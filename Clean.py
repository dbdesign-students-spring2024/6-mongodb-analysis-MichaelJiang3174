import csv
import re

def clean_html_tags(text):
    """Remove HTML tags from text."""
    return re.sub(r'<[^>]+>', '', text)

def clean_price(price):
    """Remove dollar sign and commas from price and convert to float."""
    return float(re.sub(r'[$,]', '', price))

def clean_amenities(amenities):
    """Clean and convert amenities list from string to list."""
    # Removing the leading and trailing square brackets and splitting by ', '
    amenities = amenities.strip('[]').split(', ')
    # Removing quotes from each amenity
    amenities = [amenity.strip('"') for amenity in amenities]
    return amenities

def clean_data_with_csv(file_path, clean_file_path):
    with open(file_path, newline='', encoding='utf-8', errors='ignore') as infile, \
         open(clean_file_path, 'w', newline='', encoding='utf-8') as outfile:
        
        reader = csv.DictReader(infile)
        fieldnames = reader.fieldnames
        
        writer = csv.DictWriter(outfile, fieldnames=fieldnames)
        writer.writeheader()

        for row in reader:
            # Cleaning operations
            row['description'] = clean_html_tags(row['description'])
            if row['price']:
                row['price'] = clean_price(row['price'])
            if row['amenities']:
                row['amenities'] = clean_amenities(row['amenities'])
            
            writer.writerow(row)


# Redefining the clean file path in case it's needed for reference
file_path = '/Users/michael/Desktop/Database design and implementation/6-mongodb-analysis-MichaelJiang3174/data/listings.csv'
clean_file_path = 'data/listings_clean.csv'

# Performing the cleaning using the revised approach
clean_data_with_csv(file_path, clean_file_path)
