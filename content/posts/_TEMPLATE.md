---
title: "Your Post Title Here"
date: 2025-12-04T10:30:00.000Z
updated: 2025-12-04T10:30:00.000Z
categories: ["Category Name"]
tags: ["tag1", "tag2", "tag3"]
featured_image: "your-image.jpg"
excerpt: "A brief 1-2 sentence description of your post that appears in listings"
---

# Main Heading

Write your introduction here. This is the opening paragraph that hooks your readers.

## Section 1

Your content here with **bold text** and *italic text*.

### Subsection

You can create nested sections.

## Code Examples

Inline code: `print("Hello, World!")`

Code block:

```python
def hello_world():
    print("Hello, World!")
    return True
```

```javascript
function helloWorld() {
    console.log("Hello, World!");
}
```

## Lists

Unordered list:
- Item 1
- Item 2
- Item 3

Ordered list:
1. First item
2. Second item
3. Third item

## Links and Images

[Link text](https://example.com)

![Alt text for image](/images/your-image.jpg)

## Quotes

> This is a blockquote.
> It can span multiple lines.

## Tables

| Column 1 | Column 2 | Column 3 |
|----------|----------|----------|
| Data 1   | Data 2   | Data 3   |
| Data 4   | Data 5   | Data 6   |

## Emphasis

**Bold text**
*Italic text*
***Bold and italic***
~~Strikethrough~~

## Conclusion

Wrap up your post with a conclusion.

---

## Notes for Authors

### Frontmatter Fields:

- `title`: Your post title (required)
- `date`: Publication date in YYYY-MM-DD format (required)
- `updated`: Last updated date (optional, defaults to date)
- `categories`: Array of categories (must match `backend/metadata/categories.json`)
- `tags`: Array of tags (must match `backend/metadata/tags.json`)
- `featured_image`: Filename of image in `images/` directory (optional)
- `excerpt`: Brief description for post listings (optional)

### Filename Convention:

Save as: `content/posts/YYYY-MM-DD-your-post-slug.md`

Example: `content/posts/2025-12-04-my-awesome-post.md`

### Images:

1. Place images in `images/` directory
2. Reference in frontmatter: `featured_image: "filename.jpg"`
3. Reference in content: `![Alt](/images/filename.jpg)`

### After Writing:

1. Save your markdown file
2. Build: `./build.sh`
3. Preview: `cd frontend/dist && python3 -m http.server 8000`
4. Commit: `git add . && git commit -m "Add new post"`
5. Push: `git push origin master`

### Tips:

- Keep filenames lowercase with hyphens
- Use descriptive slugs
- Add relevant tags for discoverability
- Write compelling excerpts
- Optimize images before uploading
- Preview locally before deploying
