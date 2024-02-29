# Restaurant Data Scraper

This repository contains Python scripts to scrape restaurant data from the web, update CSV files with full URLs, and extract menu data.

## Scripts

### 1. Scrape Restaurant Data

The `scrape_restaurant_data.py` script scrapes restaurant data from a given URL and prints the extracted information.

#### Usage

```bash
python scrape_restaurant_data.py
```

#### Dependencies

- requests
- BeautifulSoup

### 2. Scrape and Store Restaurant Data

The `scrape_and_store_restaurant_data.py` script scrapes restaurant data from a given URL and stores it in a CSV file named `restaurant_data.csv`.

#### Usage

```bash
python scrape_and_store_restaurant_data.py
```

#### Dependencies

- requests
- BeautifulSoup
- csv

### 3. Update CSV with Full URLs

The `update_csv_with_full_urls.py` script updates a CSV file containing partial URLs with their full URLs and stores the updated data in the same CSV file.

#### Usage

```bash
python update_csv_with_full_urls.py
```

#### Dependencies

- csv
- os

### 4. Extract and Store Menu Data

The `extract_and_store_menu_data.py` script extracts menu data from URLs provided in a CSV file and stores the extracted data in a new CSV file named `menu_data.csv`.

#### Usage

```bash
python extract_and_store_menu_data.py
```

#### Dependencies

- csv
- requests
- BeautifulSoup

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE)