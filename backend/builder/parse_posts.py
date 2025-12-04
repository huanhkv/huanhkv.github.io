"""
Parse markdown posts with frontmatter
"""
import os
import re
from pathlib import Path
from datetime import datetime
import markdown
from markdown.extensions import fenced_code, tables, codehilite

# Paths
PROJECT_ROOT = Path(__file__).parent.parent.parent
POSTS_DIR = PROJECT_ROOT / "content" / "posts"

def parse_frontmatter(content):
    """Extract YAML frontmatter from markdown"""
    frontmatter = {}
    body = content
    
    # Match frontmatter pattern
    pattern = r'^---\s*\n(.*?)\n---\s*\n(.*)$'
    match = re.match(pattern, content, re.DOTALL)
    
    if match:
        frontmatter_str = match.group(1)
        body = match.group(2)
        
        # Parse simple YAML (key: value pairs)
        for line in frontmatter_str.split('\n'):
            if ':' in line:
                key, value = line.split(':', 1)
                key = key.strip()
                value = value.strip()
                
                # Handle lists (e.g., categories: ["a", "b"])
                if value.startswith('[') and value.endswith(']'):
                    value = [item.strip(' "\'') for item in value[1:-1].split(',')]
                else:
                    value = value.strip('"\'')
                
                frontmatter[key] = value
    
    return frontmatter, body

def slugify(text):
    """Convert text to URL-friendly slug"""
    text = text.lower()
    text = re.sub(r'[^\w\s-]', '', text)
    text = re.sub(r'[\s_-]+', '-', text)
    return text.strip('-')

def markdown_to_html(markdown_text):
    """Convert markdown to HTML"""
    md = markdown.Markdown(extensions=[
        'fenced_code',
        'tables',
        'codehilite',
        'nl2br',
        'sane_lists'
    ])
    return md.convert(markdown_text)

def parse_post(file_path):
    """Parse a single markdown post"""
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    frontmatter, body = parse_frontmatter(content)
    html_content = markdown_to_html(body)
    
    # Extract filename for slug
    filename = Path(file_path).stem
    
    post = {
        'title': frontmatter.get('title', 'Untitled'),
        'date': frontmatter.get('date', ''),
        'updated': frontmatter.get('updated', ''),
        'categories': frontmatter.get('categories', []),
        'tags': frontmatter.get('tags', []),
        'featured_image': frontmatter.get('featured_image', ''),
        'excerpt': frontmatter.get('excerpt', ''),
        'content': html_content,
        'slug': filename,
        'filename': filename
    }
    
    return post

def parse_all_posts():
    """Parse all markdown posts in the posts directory"""
    posts = []
    
    if not POSTS_DIR.exists():
        print(f"⚠️  Posts directory not found: {POSTS_DIR}")
        return posts
    
    for file_path in sorted(POSTS_DIR.glob("*.md"), reverse=True):
        try:
            post = parse_post(file_path)
            posts.append(post)
        except Exception as e:
            print(f"❌ Error parsing {file_path}: {e}")
    
    return posts

if __name__ == "__main__":
    # Test parsing
    posts = parse_all_posts()
    print(f"Found {len(posts)} posts")
    for post in posts:
        print(f"- {post['title']} ({post['date']})")
