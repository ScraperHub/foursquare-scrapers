from crawlbase import CrawlingAPI
from bs4 import BeautifulSoup
import json

# Initialize Crawlbase API with your access token
crawling_api = CrawlingAPI({'token': 'YOUR_CRAWLBASE_TOKEN'})

def make_crawlbase_request_with_pagination(url):
    options = {
        'ajax_wait': 'true',
        'page_wait': '5000',
        'css_click_selector': 'li.moreResults > button'
    }

    response = crawling_api.get(url, options)

    if response['headers']['pc_status'] == '200':
        html_content = response['body'].decode('utf-8')
        return html_content
    else:
        print(f"Failed to fetch the page. Crawlbase status code: {response['headers']['pc_status']}")
        return None

def scrape_foursquare_listings(html_content):
    soup = BeautifulSoup(html_content, 'html.parser')
    data = []

    # Select all place listings
    listings = soup.select('ul.recommendationList > li.singleRecommendation')

    for listing in listings:
        name = listing.select_one('div.venueName a').text.strip() if listing.select_one('div.venueName a') else ''
        address = listing.select_one('div.venueAddress').text.strip() if listing.select_one('div.venueAddress') else ''
        category = listing.select_one('span.categoryName').text.strip() if listing.select_one('span.categoryName') else ''
        link = listing.select_one('div.venueName a')['href'] if listing.select_one('div.venueName a') else ''

        # Add extracted data to the list
        data.append({
            'name': name,
            'address': address,
            'category': category,
            'link': f"https://foursquare.com{link}"  # Construct the full URL
        })

    return data

def save_data_to_json(data, filename='foursquare_data.json'):
    with open(filename, 'w') as f:
        json.dump(data, f, indent=4)
    print(f"Data saved to {filename}")

if __name__ == "__main__":
    url = "https://foursquare.com/explore?near=New%20York&q=Food"
    html_content = make_crawlbase_request_with_pagination(url)

    if html_content:
        data = scrape_foursquare_listings(html_content)  # Extract data from HTML content
        save_data_to_json(data)