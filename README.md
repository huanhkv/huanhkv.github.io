# Reideen's Blog

Static blog generator with markdown posts. Ready to evolve into a dynamic site.

## Quick Start

```bash
make build      # Build site
make serve      # Build and preview at localhost:8000
make help       # Show all commands
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
│   └── builder/             # Build scripts
├── frontend/
│   ├── dist/                # Generated site (deployed)
│   ├── templates/           # HTML templates
│   └── assets/              # CSS, JS
```

## Create New Post

Create `content/posts/YYYY-MM-DD-title.md`:

```markdown
---
title: "Post Title"
date: 2025-12-04T10:30:00.000Z
categories: ["Computer Science"]
tags: ["tutorial"]
featured_image: "image.jpg"
excerpt: "Brief description"
---

Your markdown content here...
```

Then run `make build` and push to deploy.

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