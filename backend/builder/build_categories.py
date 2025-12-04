"""
Build category pages
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

def build_category_pages(posts):
    """Build a page for each category"""
    template = env.get_template('category.html')
    
    # Load categories metadata
    categories_path = CONTENT_DIR / "categories.json"
    with open(categories_path, 'r', encoding='utf-8') as f:
        categories_data = json.load(f)['categories']
    
    # Group posts by category
    posts_by_category = defaultdict(list)
    for post in posts:
        for cat in post.get('categories', []):
            posts_by_category[cat.lower()].append(post)
    
    # Create categories directory
    categories_dir = DIST_DIR / "categories"
    categories_dir.mkdir(exist_ok=True)
    
    # Render each category page
    for category_data in categories_data:
        cat_slug = category_data['slug']
        cat_posts = posts_by_category.get(cat_slug.lower(), [])
        
        html = template.render(
            category=category_data,
            posts=cat_posts
        )
        
        output_path = categories_dir / f"{cat_slug}.html"
        output_path.write_text(html, encoding='utf-8')
    
    print(f"  ✓ {len(categories_data)} category pages")

if __name__ == "__main__":
    from parse_posts import parse_all_posts
    posts = parse_all_posts()
    build_category_pages(posts)
