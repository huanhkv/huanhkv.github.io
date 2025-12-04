"""
Build tag pages
"""
import json
from pathlib import Path
from collections import defaultdict
from jinja2 import Environment, FileSystemLoader

# Paths
PROJECT_ROOT = Path(__file__).parent.parent.parent
TEMPLATES_DIR = PROJECT_ROOT / "frontend" / "templates"
DIST_DIR = PROJECT_ROOT / "frontend" / "dist"
CONTENT_DIR = PROJECT_ROOT / "content"

# Setup Jinja2
env = Environment(loader=FileSystemLoader(TEMPLATES_DIR))

def build_tag_pages(posts):
    """Build a page for each tag"""
    template = env.get_template('tag.html')
    
    # Load tags metadata
    tags_path = CONTENT_DIR / "tags.json"
    with open(tags_path, 'r', encoding='utf-8') as f:
        tags_data = json.load(f)['tags']
    
    # Group posts by tag
    posts_by_tag = defaultdict(list)
    for post in posts:
        for tag in post.get('tags', []):
            posts_by_tag[tag.lower()].append(post)
    
    # Create tags directory
    tags_dir = DIST_DIR / "tags"
    tags_dir.mkdir(exist_ok=True)
    
    # Render each tag page
    for tag_data in tags_data:
        tag_slug = tag_data['slug']
        tag_posts = posts_by_tag.get(tag_slug.lower(), [])
        
        html = template.render(
            tag=tag_data,
            posts=tag_posts
        )
        
        output_path = tags_dir / f"{tag_slug}.html"
        output_path.write_text(html, encoding='utf-8')
    
    print(f"  ✓ {len(tags_data)} tag pages")

if __name__ == "__main__":
    from parse_posts import parse_all_posts
    posts = parse_all_posts()
    build_tag_pages(posts)
