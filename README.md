# IGAC Mwea — Static Website

This is a small static website for International Gospel Acts Church — Mwea Branch.

Quick notes:
- It's a static site (HTML, CSS, JS, JSON data). No build step required.
- Data (events, gallery, sermons, leadership, etc.) are read from the `data/` JSON files.
- Replace the placeholder Formspree IDs and donation links before publishing.

How to preview locally
- From the project root run a simple HTTP server (fetch won't work from `file://`):

```powershell
# Python 3 (Windows / macOS / Linux)
python -m http.server 8000
# then open http://localhost:8000
```

Recommended publishing options
- GitHub Pages: push this repo and enable Pages from branch `main` (or use `/docs` folder).
- Netlify / Vercel: connect the repo — they serve static sites automatically.
- Manual: upload the repository files to any static host or S3/Cloudflare Pages.

Checklist before publishing
- Replace `action="https://formspree.io/f/your-form-id"` and the newsletter `formspree` id in `index.html`.
- Confirm online payment links (PayPal / M‑Pesa) are correct and secure.
- Verify `data/config.json` `live` settings and `mapEmbed` (either a URL or an iframe string).
- Confirm all images referenced in `data/` and `index.html` exist in the repo (they do in this copy).
- Serve the site over HTTP when testing (see preview command above).

Other suggestions
- Consider adding a `CNAME` if you have a custom domain and configuring TLS on your host.
- Add a small `LICENSE` and update metadata (site title, description) in `index.html` for SEO.
- Optionally add a `robots.txt` and `sitemap.xml` if you expect search indexing.

If you'd like, I can:
- Create a `package.json` and small deploy script for Netlify/Vercel, or
- Configure a GitHub Actions workflow to automatically publish to GitHub Pages.
