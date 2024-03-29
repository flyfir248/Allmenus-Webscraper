import csv


def update_csv_with_full_urls(csv_file):
    # Open the CSV file for reading and writing
    with open(csv_file, 'r', newline='', encoding='utf-8') as file:
        reader = csv.DictReader(file)

        # Define the fieldnames including the new column
        fieldnames = reader.fieldnames + ['Full_URL']

        # Open a temporary file to write the updated data
        with open('temp.csv', 'w', newline='', encoding='utf-8') as temp_file:
            writer = csv.DictWriter(temp_file, fieldnames=fieldnames)
            writer.writeheader()

            # Update each row with the full URL and write to the temporary file
            for row in reader:
                full_url = f"https://www.allmenus.com{row['URL']}"
                row['Full_URL'] = full_url
                writer.writerow(row)

    # Replace the original file with the temporary file
    import os
    os.replace('temp.csv', csv_file)


if __name__ == "__main__":
    csv_file = 'restaurant_data.csv'
    update_csv_with_full_urls(csv_file)
