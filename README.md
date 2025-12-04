# Reideen's Blog

Static blog generator with markdown posts. Ready to evolve into a dynamic site.

## Quick Start

**Build site:**
```bash
make build
# or: ./build.sh (legacy)
```

**Preview locally:**
```bash
make serve
# or: cd frontend/dist && python3 -m http.server 8000
```

**Development mode:**
```bash
make dev        # Serve without rebuilding
make watch      # Auto-rebuild on file changes (requires fswatch)
```

**Other commands:**
```bash
make help       # Show all available commands
make clean      # Clean build output
make install    # Install dependencies
make check      # Check required tools
```

**Deploy:** Push to GitHub (auto-deploys via Actions)

## Structure

```
├── content/                  # All site content
│   ├── posts/               # Write .md posts here
│   ├── bucket/              # Bucket list
│   ├── timeline/            # Timeline
│   ├── images/              # Image files
│   ├── categories.json      # Categories
│   └── tags.json            # Tags
├── backend/
│   └── scripts/             # Build scripts
├── frontend/
│   ├── dist/                # Generated site (deployed)
│   ├── templates/           # HTML templates
│   └── assets/              # CSS, JS
```

## Create New Post

1. Create: `content/posts/YYYY-MM-DD-title.md`
2. Add frontmatter:

```markdown
---
title: "Post Title"
date: 2025-12-04
categories: ["Computer Science"]
tags: ["tutorial"]
featured_image: "image.jpg"
excerpt: "Brief description"
---

Your markdown content here...
```

3. Build: `./build.sh`
4. Push to deploy

## Content Files

- **Posts**: `content/posts/*.md`
- **Categories**: `content/categories.json`
- **Tags**: `content/tags.json`
- **Bucket List**: `content/bucket/bucket.json`
- **Timeline**: `content/timeline/timeline.json`

## Setup GitHub Pages

1. Repository Settings → Pages
2. Source: **GitHub Actions**
3. Push to master to deploy

---

**Phase 2 Ready**: Structure prepared for FastAPI/Flask backend + React/Vue frontend