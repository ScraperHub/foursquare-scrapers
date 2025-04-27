# foursquare-data-scraper

## Description

This repository contains two Python scrapers for extracting data from Foursquare — a search listings scraper and a venue detail page scraper. Both scrapers use the [Crawlbase Crawling API](https://crawlbase.com/crawling-api-avoid-captchas-blocks) to bypass JavaScript rendering issues, infinite scroll, CAPTCHAs, and other anti-bot mechanisms.

➡ Read the full blog [here](https://crawlbase.com/blog/how-to-extract-foursquare-data/) to learn more.

## Scraper Overview

### 1. Foursquare Search Listing Scraper

The `foursquare_listing_scraper.py` extracts:

- **Venue Name**
- **Address**
- **Category**
- **Venue Profile URL**

It supports infinite scrolling to load and capture all listings for a given search query.

### 2. Foursquare Venue Detail Page Scraper

The `foursquare_venue_detail_scraper.py` extracts:

- **Venue Name**
- **Address**
- **Phone Number**
- **Rating**
- **Ratings Count**

Perfect for gathering detailed information about a specific venue.

## Environment Setup

Make sure you have Python 3.7 or higher installed:

```bash
python --version
```

Install the required libraries:

```bash
pip install crawlbase beautifulsoup4
```

- **Crawlbase** – Handles dynamic page loads and avoids blocks.
- **BeautifulSoup** – Parses and extracts HTML content.

## Running the Scrapers

### 1. Running the Search Listings Scraper

- **Get Your Crawlbase Access Token**
  Sign up at [Crawlbase](https://crawlbase.com/signup) to get your API token.

- **Update Your Token**

  - Replace `"YOUR_CRAWLBASE_TOKEN"` in `foursquare_listing_scraper.py` with your actual token.

- **Run the Scraper**

  ```bash
  python foursquare_listing_scraper.py
  ```

The extracted data will be saved in `foursquare_listing_data.json`.

## 2. Running the Venue Detail Scraper

- **Get Your Crawlbase Access Token**
- **Update Your Token**
  Replace `"YOUR_CRAWLBASE_TOKEN"` in `foursquare_venue_detail_scraper.py`.

- **Run the Scraper**
  `bash
  python foursquare_venue_detail_scraper.py
  `
  The venue details will be saved in `foursquare_venue_details.json`.

## To-Do List

- Add CLI support to scrape multiple venue URLs in batch.
- Export listing and venue data to CSV as an additional format.
- Implement retry logic for failed or incomplete responses.
