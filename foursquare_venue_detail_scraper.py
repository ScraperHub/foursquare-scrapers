from crawlbase import CrawlingAPI
from bs4 import BeautifulSoup
import json

# Initialize Crawlbase API with your token
crawling_api = CrawlingAPI({'token': 'YOUR_CRAWLBASE_TOKEN'})

def fetch_venue_details(url):
    # Crawlbase request options
    options = {
        'ajax_wait': 'true',  # Wait for JavaScript to load
        'page_wait': '5000'   # Wait 5 seconds for full page render
    }

    response = crawling_api.get(url, options)

    if response['headers']['pc_status'] == '200':
        html_content = response['body'].decode('utf-8')
        return html_content
    else:
        print(f"Error fetching venue details. Status: {response['headers']['pc_status']}")
        return None

def scrape_venue_details(html_content):
    soup = BeautifulSoup(html_content, 'html.parser')

    # Extract venue details
    name = soup.select_one('h1.venueName').text.strip() if soup.select_one('h1.venueName') else ''
    address = soup.select_one('div.venueAddress').text.strip() if soup.select_one('div.venueAddress') else ''
    phone = soup.select_one('span[itemprop="telephone"]').text.strip() if soup.select_one('span[itemprop="telephone"]') else ''
    rating = soup.select_one('span[itemprop="ratingValue"]').text.strip() if soup.select_one('span[itemprop="ratingValue"]') else ''
    ratings_count = soup.select_one('div.numRatings').text.strip() if soup.select_one('div.numRatings') else ''

    # Return the details in a dictionary
    return {
        'name': name,
        'address': address,
        'phone': phone,
        'rating': rating,
        'ratings_count': ratings_count
    }

def save_venue_data(data, filename='foursquare_venue_details.json'):
    with open(filename, 'w') as f:
        json.dump(data, f, indent=4)
    print(f"Data successfully saved to {filename}")

# Example usage:
if __name__ == "__main__":
    url = 'https://foursquare.com/v/thai-diner/5e46e2ec5791a10008c55728'
    html_content = fetch_venue_details(url)

    if html_content:
        venue_data = scrape_venue_details(html_content)
        save_venue_data(venue_data)