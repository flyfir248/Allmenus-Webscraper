import csv
import requests
from bs4 import BeautifulSoup


def extract_menu_data(url):
    # Send a GET request to the URL
    response = requests.get(url)

    # Check if the request was successful
    if response.status_code == 200:
        # Parse the HTML content using BeautifulSoup
        soup = BeautifulSoup(response.text, 'html.parser')

        # Find all menu items
        menu_items = soup.find_all('li', class_='menu-items')

        # Extract menu item names and prices
        menu_data = []
        for item in menu_items:
            item_name = item.find('span', class_='item-title').text.strip()
            item_price = item.find('span', class_='item-price').text.strip()
            menu_data.append({'Item': item_name, 'Price': item_price})

        return menu_data
    else:
        print("Failed to retrieve data. Status code:", response.status_code)
        return None


def extract_and_store_menu_data(csv_file):
    # Open the CSV file for reading
    with open(csv_file, 'r', newline='', encoding='utf-8') as file:
        reader = csv.DictReader(file)

        # Open a new CSV file to store the extracted menu data
        with open('menu_data.csv', 'w', newline='', encoding='utf-8') as csvfile:
            fieldnames = ['Restaurant', 'Item', 'Price']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()

            # Iterate through each row in the CSV file
            for row in reader:
                restaurant_name = row['Name']
                restaurant_url = row['URL']

                # If the URL is not empty, extract menu data
                if restaurant_url:
                    full_url = f"https://www.allmenus.com{restaurant_url}"
                    menu_data = extract_menu_data(full_url)

                    # Write menu data to CSV file
                    if menu_data:
                        for menu_item in menu_data:
                            menu_item['Restaurant'] = restaurant_name
                            writer.writerow(menu_item)


if __name__ == "__main__":
    csv_file = 'temp.csv'
    extract_and_store_menu_data(csv_file)
