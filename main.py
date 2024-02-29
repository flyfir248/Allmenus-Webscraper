import requests
from bs4 import BeautifulSoup


def scrape_restaurant_data(url):
    # Send a GET request to the URL
    response = requests.get(url)

    # Check if the request was successful
    if response.status_code == 200:
        # Parse the HTML content using BeautifulSoup
        soup = BeautifulSoup(response.text, 'html.parser')

        # Find all divs with class 's-row'
        restaurant_divs = soup.find_all('div', class_='s-row')

        # Extract restaurant details
        for restaurant_div in restaurant_divs:
            # Restaurant name and URL
            restaurant_name_tag = restaurant_div.find('h4', class_='name')
            restaurant_name = restaurant_name_tag.text.strip() if restaurant_name_tag else None
            restaurant_url = restaurant_name_tag.a['href'] if restaurant_name_tag else None
            # Cuisine
            cuisine_tag = restaurant_div.find('p', class_='cuisine-list')
            cuisine = cuisine_tag.text.strip() if cuisine_tag else None
            # Address
            address_tags = restaurant_div.find_all('p', class_='address')
            address = ', '.join(tag.text.strip() for tag in address_tags) if address_tags else None
            # Print extracted data
            print("Name:", restaurant_name)
            print("URL:", restaurant_url)
            print("Cuisine:", cuisine)
            print("Address:", address)
            print()
    else:
        print("Failed to retrieve data. Status code:", response.status_code)


if __name__ == "__main__":
    # URL of the page containing restaurant data
    url = "https://www.allmenus.com/ny/new-york/-/"

    # Scrape restaurant data
    scrape_restaurant_data(url)
