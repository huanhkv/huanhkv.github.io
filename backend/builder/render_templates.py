"""
Render HTML pages using Jinja2 templates
"""
import json
from pathlib import Path
from jinja2 import Environment, FileSystemLoader

# Paths
PROJECT_ROOT = Path(__file__).parent.parent.parent
TEMPLATES_DIR = PROJECT_ROOT / "frontend" / "templates"
DIST_DIR = PROJECT_ROOT / "frontend" / "dist"
CONTENT_DIR = PROJECT_ROOT / "content"

# Setup Jinja2
env = Environment(loader=FileSystemLoader(TEMPLATES_DIR))

def load_metadata():
    """Load categories, tags, bucket list, and timeline"""
    metadata = {}
    
    # Load categories
    categories_path = CONTENT_DIR / "categories.json"
    if categories_path.exists():
        with open(categories_path, 'r', encoding='utf-8') as f:
            metadata['categories'] = json.load(f)['categories']
    
    # Load tags
    tags_path = CONTENT_DIR / "tags.json"
    if tags_path.exists():
        with open(tags_path, 'r', encoding='utf-8') as f:
            metadata['tags'] = json.load(f)['tags']
    
    # Load bucket list
    bucket_path = CONTENT_DIR / "bucket" / "bucket.json"
    if bucket_path.exists():
        with open(bucket_path, 'r', encoding='utf-8') as f:
            metadata['bucket_list'] = json.load(f)['bucket_list']
    
    # Load timeline
    timeline_path = CONTENT_DIR / "timeline" / "timeline.json"
    if timeline_path.exists():
        with open(timeline_path, 'r', encoding='utf-8') as f:
            metadata['timeline'] = json.load(f)['timeline']
    
    return metadata

def render_index(posts):
    """Render index/home page"""
    template = env.get_template('index.html')
    metadata = load_metadata()
    
    html = template.render(
        posts=posts,
        categories=metadata.get('categories', []),
        tags=metadata.get('tags', [])
    )
    
    output_path = DIST_DIR / "index.html"
    output_path.write_text(html, encoding='utf-8')
    print(f"  ✓ index.html")

def render_posts(posts):
    """Render individual post pages"""
    template = env.get_template('post.html')
    posts_dir = DIST_DIR / "posts"
    posts_dir.mkdir(exist_ok=True)
    
    for post in posts:
        html = template.render(post=post)
        output_path = posts_dir / f"{post['slug']}.html"
        output_path.write_text(html, encoding='utf-8')
    
    print(f"  ✓ {len(posts)} post pages")

def render_bucket():
    """Render bucket list page"""
    template = env.get_template('bucket.html')
    metadata = load_metadata()
    
    html = template.render(bucket_list=metadata.get('bucket_list', []))
    
    output_path = DIST_DIR / "bucket.html"
    output_path.write_text(html, encoding='utf-8')
    print(f"  ✓ bucket.html")

def render_timeline():
    """Render timeline page"""
    template = env.get_template('timeline.html')
    metadata = load_metadata()
    
    # Sort timeline by date (newest first)
    timeline = sorted(
        metadata.get('timeline', []),
        key=lambda x: x['date'],
        reverse=True
    )
    
    html = template.render(timeline=timeline)
    
    output_path = DIST_DIR / "timeline.html"
    output_path.write_text(html, encoding='utf-8')
    print(f"  ✓ timeline.html")

def render_about():
    """Render about page"""
    template = env.get_template('about.html')
    
    html = template.render()
    
    output_path = DIST_DIR / "about.html"
    output_path.write_text(html, encoding='utf-8')
    print(f"  ✓ about.html")

def render_all_pages(posts):
    """Render all pages"""
    render_index(posts)
    render_posts(posts)
    render_bucket()
    render_timeline()
    render_about()

if __name__ == "__main__":
    from parse_posts import parse_all_posts
    posts = parse_all_posts()
    render_all_pages(posts)
