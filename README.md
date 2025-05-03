# Firecrawl Content Extractor

This Python script is a utility tool designed to extract **only the main content** (in Markdown format) from a list of web pages using the [Firecrawl API](https://firecrawl.dev/). It’s ideal for developers or researchers looking to **scrape article-like content** without all the extra page noise (ads, navbars, etc.).

> ⚙️ This project fits into a niche space in web scraping — extracting **semantic, clean content** from webpages using a headless browser + AI combination (via Firecrawl).

---

## Features

- Parses URLs from a CSV file
- Sends structured POST requests to Firecrawl
- Extracts and saves clean Markdown content into individual `.txt` files
- Handles missing or malformed API responses gracefully
- Easily extendable for JSON output or further processing

---

## 📦 Usage

### 1. Add Your API Key
Edit the script and add your Firecrawl API key:
```python
"Authorization": "Bearer fc-<YOUR_API_KEY>"
