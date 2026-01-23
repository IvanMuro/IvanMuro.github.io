# Academic Website - Dr. Iván Muñoz Rodríguez

A professional academic website built with Jekyll for GitHub Pages. Clean, minimal design with dark mode support, optimised for academic discoverability.

## Quick Start (GitHub Pages Deployment)

### 1. Create Your Repository

1. Go to [GitHub](https://github.com) and create a new repository
2. Name it `IvanMuro.github.io` (replace `IvanMuro` with your GitHub username)
3. Make it **Public**

### 2. Upload Your Site

Option A - **Using GitHub's web interface** (easiest):
1. Click "uploading an existing file" on the repository page
2. Drag and drop all the files from this folder
3. Click "Commit changes"

Option B - **Using Git command line**:
```bash
cd /path/to/this/folder
git init
git add .
git commit -m "Initial website setup"
git branch -M main
git remote add origin https://github.com/IvanMuro/IvanMuro.github.io.git
git push -u origin main
```

### 3. Enable GitHub Pages

1. Go to your repository's **Settings** → **Pages**
2. Under "Source", select **main** branch
3. Click **Save**
4. Your site will be live at `https://IvanMuro.github.io` within a few minutes!

---

## Configuration

### Essential Settings

Edit `_config.yml` to personalise your site:

```yaml
# Update these with your information
title: "Dr. Iván Muñoz Rodríguez"
url: "https://IvanMuro.github.io"  # Your GitHub Pages URL
repository: "IvanMuro/IvanMuro.github.io"

author:
  name: "Iván Muñoz Rodríguez"
  email: "ivan.munozrodriguez@cea.fr"
  orcid: "0000-0001-7161-4112"
  github: "IvanMuro"
  ads_library: "https://ui.adsabs.harvard.edu/user/libraries/pwMQA74QTmC-ylWwtp4nWQ"
```

### Feature Toggles

```yaml
features:
  dark_mode: true        # Enable/disable dark mode toggle
  blog_enabled: false    # Set to true to activate the blog
  reading_list: false    # Show "Currently Reading" section (not yet implemented)
```

---

## Content Management

### Updating Pages

All content is in simple Markdown files. Just edit these files directly:

| Page | File | What to Edit |
|------|------|--------------|
| Home | `index.md` | Hero section, intro text, research interests |
| Research | `research.md` | Projects, research areas, collaborations |
| Publications | `publications.md` | Publication list, links |
| CV | `cv.md` | Education, experience, skills |
| Contact | `contact.md` | Contact info, address |

### Adding Your Photo

1. Prepare a square photo (recommended: 600×600 pixels)
2. Name it `profile.jpg`
3. Upload to `assets/images/profile.jpg`

### Adding Your CV PDF

1. Export your CV as PDF
2. Name it `cv_munoz_rodriguez.pdf` (or update the link in `cv.md`)
3. Upload to `assets/cv/cv_munoz_rodriguez.pdf`

### Enabling the Blog

1. In `_config.yml`, set:
   ```yaml
   features:
     blog_enabled: true
   ```

2. Uncomment the blog link in navigation:
   ```yaml
   navigation:
     - title: About
       url: /
     - title: Research
       url: /research/
     - title: Publications
       url: /publications/
     - title: CV
       url: /cv/
     - title: Blog        # Uncomment this
       url: /blog/        # and this
     - title: Contact
       url: /contact/
   ```

### Creating Blog Posts

1. Create a new file in `_posts/` with the format:
   ```
   YYYY-MM-DD-title-of-post.md
   ```
   Example: `2025-01-20-new-paper-published.md`

2. Add front matter at the top:
   ```yaml
   ---
   layout: post
   title: "Your Post Title"
   date: 2025-01-20
   categories: [research]
   tags: [x-ray, clusters, publication]
   excerpt: "A brief summary of your post."
   ---

   Your content here in Markdown...
   ```

### Daily Quote Feature

The home page displays a random quote that changes each day. Everyone visiting the site sees the same quote on the same day.

#### Option A: Local File (Default)

Edit `_data/quotes.yml` to manage your quotes:

```yaml
- text: "Your quote text here"
  author: "Author Name"
  source: "Optional source (book, speech, etc.)"

- text: "Another quote"
  author: "Another Author"
```

#### Option B: Google Sheets

If you prefer to manage quotes from a Google Doc/Sheet:

1. Create a Google Sheet with three columns: `text`, `author`, `source`
2. Add your quotes (one per row, skip the header row)
3. Go to **File → Share → Publish to web**
4. Select your sheet tab and choose **Comma-separated values (.csv)**
5. Click **Publish** and copy the URL
6. In `index.md`, change:
   ```liquid
   {% include daily-quote.html %}
   ```
   to:
   ```liquid
   {% include daily-quote-google.html %}
   ```
7. In `_includes/daily-quote-google.html`, replace `YOUR_GOOGLE_SHEET_CSV_URL_HERE` with your URL

#### Removing the Daily Quote

To remove this feature, simply delete this line from `index.md`:
```liquid
{% include daily-quote.html %}
```

---

## Customisation

### Changing Colours

Edit `_sass/_variables.scss` to modify the colour scheme:

```scss
// Light Theme - Primary colours
--color-primary: #1a365d;      // Deep navy (headings, links)
--color-accent: #c05621;       // Terracotta (highlights)

// Dark Theme
[data-theme="dark"] {
  --color-primary: #90cdf4;    // Light blue
  --color-accent: #f6ad55;     // Warm orange
}
```

### Changing Fonts

In `_includes/head.html`, modify the Google Fonts link:

```html
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600&family=Source+Serif+4:opsz,wght@8..60,400;8..60,600;8..60,700&display=swap" rel="stylesheet">
```

Then update `_sass/_variables.scss`:

```scss
--font-serif: 'Source Serif 4', Georgia, serif;
--font-sans: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
```

### Adding Social Links

In `_config.yml`:

```yaml
author:
  twitter: "yourtwitterhandle"      # Add Twitter
  linkedin: "yourlinkedinprofile"   # Add LinkedIn
  google_scholar: "https://scholar.google.com/citations?user=XXXXXXX"
```

Then update `_includes/footer.html` to display them.

---

## File Structure

```
.
├── _config.yml           # Site configuration
├── _layouts/             # Page templates
│   ├── default.html      # Base layout
│   ├── home.html         # Home page layout
│   ├── page.html         # Standard page layout
│   └── post.html         # Blog post layout
├── _includes/            # Reusable components
│   ├── head.html         # Meta tags, CSS links
│   ├── header.html       # Navigation
│   ├── footer.html       # Footer with links
│   └── daily-quote.html  # Daily quote component
├── _data/                # Data files
│   └── quotes.yml        # Daily quotes collection
├── _sass/                # Stylesheets
│   ├── _variables.scss   # Colours, fonts, spacing
│   ├── _base.scss        # Base styles
│   ├── _layout.scss      # Layout styles
│   └── _components.scss  # Component styles
├── _posts/               # Blog posts
├── assets/
│   ├── css/main.scss     # Main stylesheet
│   ├── images/           # Images (profile.jpg, etc.)
│   └── cv/               # CV PDF
├── index.md              # Home page
├── research.md           # Research page
├── publications.md       # Publications page
├── cv.md                 # CV page
├── contact.md            # Contact page
├── blog.md               # Blog listing
├── Gemfile               # Ruby dependencies
└── README.md             # This file
```

---

## Local Development (Optional)

If you want to preview changes locally before pushing:

### Prerequisites

1. Install Ruby (version 2.7 or higher)
2. Install Bundler: `gem install bundler`

### Setup

```bash
cd /path/to/website
bundle install
```

### Run Local Server

```bash
bundle exec jekyll serve
```

Then open `http://localhost:4000` in your browser.

### Live Reload

For automatic refresh on changes:

```bash
bundle exec jekyll serve --livereload
```

---

## Maintenance Checklist

### Monthly
- [ ] Update publication list if new papers published
- [ ] Check all external links still work

### After Major Updates
- [ ] Update CV (both webpage and PDF)
- [ ] Review and update research project descriptions
- [ ] Add any new collaborations

### Annually
- [ ] Review overall design and content
- [ ] Update profile photo if needed
- [ ] Archive old news items

---

## Troubleshooting

### Site not updating after push?

- GitHub Pages can take 2-5 minutes to rebuild
- Check the **Actions** tab in your repository for build status
- Clear your browser cache (Ctrl/Cmd + Shift + R)

### Build failing?

- Check the **Actions** tab for error messages
- Common issues:
  - Syntax error in YAML front matter (missing quotes, wrong indentation)
  - Invalid date format in blog posts
  - Missing required fields

### Styles not applying?

- Make sure the front matter dashes `---` are present at the top of `.scss` files
- Check for SCSS syntax errors

### Images not showing?

- Verify the file path is correct
- Check file extension matches exactly (case-sensitive)
- Ensure the image is committed and pushed

---

## SEO & Academic Discoverability

The site includes:

- **Schema.org structured data** for Google Scholar
- **ORCID integration** for researcher identification
- **Open Graph tags** for social media sharing
- **Semantic HTML** for accessibility and SEO
- **XML sitemap** (auto-generated)
- **RSS feed** (for blog, when enabled)

To maximise discoverability:

1. Keep your ORCID profile updated
2. Ensure publications link back to your website
3. Use consistent name formatting across platforms
4. Include relevant keywords in your research descriptions

---

## Credits

Built with:
- [Jekyll](https://jekyllrb.com/) - Static site generator
- [GitHub Pages](https://pages.github.com/) - Free hosting
- [Inter](https://rsms.me/inter/) & [Source Serif](https://github.com/adobe-fonts/source-serif) - Typography

---

## Support

For questions or issues:
- Check the [Jekyll documentation](https://jekyllrb.com/docs/)
- See [GitHub Pages documentation](https://docs.github.com/en/pages)
- Review this README's troubleshooting section

---

*Last updated: January 2025*
