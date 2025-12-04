"""
Main build script to generate static site from markdown content
"""
import os
import shutil
from pathlib import Path
from builder.parse_posts import parse_all_posts
from builder.render_templates import render_all_pages
from builder.build_categories import build_category_pages
from builder.build_tags import build_tag_pages

# Paths
PROJECT_ROOT = Path(__file__).parent.parent.parent
FRONTEND_DIST = PROJECT_ROOT / "frontend" / "dist"
FRONTEND_ASSETS = PROJECT_ROOT / "frontend" / "assets"
FRONTEND_PUBLIC = PROJECT_ROOT / "frontend" / "public"
IMAGES_DIR = PROJECT_ROOT / "content" / "images"

def clean_dist():
    """Remove and recreate dist directory"""
    if FRONTEND_DIST.exists():
        shutil.rmtree(FRONTEND_DIST)
    FRONTEND_DIST.mkdir(parents=True, exist_ok=True)
    print("✅ Cleaned dist directory")

def copy_assets():
    """Copy static assets to dist"""
    # Copy assets
    if FRONTEND_ASSETS.exists():
        shutil.copytree(FRONTEND_ASSETS, FRONTEND_DIST / "assets", dirs_exist_ok=True)
        print("✅ Copied assets")
    
    # Copy public files
    if FRONTEND_PUBLIC.exists():
        for item in FRONTEND_PUBLIC.iterdir():
            if item.is_file():
                shutil.copy2(item, FRONTEND_DIST / item.name)
        print("✅ Copied public files")
    
    # Copy images
    if IMAGES_DIR.exists():
        shutil.copytree(IMAGES_DIR, FRONTEND_DIST / "images", dirs_exist_ok=True)
        print("✅ Copied images")

def build():
    """Main build process"""
    print("🚀 Starting site build...\n")
    
    # Step 1: Clean dist directory
    clean_dist()
    
    # Step 2: Parse all markdown posts
    posts = parse_all_posts()
    print(f"✅ Parsed {len(posts)} posts\n")
    
    # Step 3: Render main pages
    render_all_pages(posts)
    print("✅ Rendered main pages\n")
    
    # Step 4: Build category pages
    build_category_pages(posts)
    print("✅ Built category pages\n")
    
    # Step 5: Build tag pages
    build_tag_pages(posts)
    print("✅ Built tag pages\n")
    
    # Step 6: Copy assets
    copy_assets()
    
    print("\n✨ Site build complete! Output in frontend/dist/")

if __name__ == "__main__":
    build()