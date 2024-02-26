#!/usr/bin/python3

import requests
from bs4 import BeautifulSoup
import csv

# Function to scrape the website
def scrape_website(url):
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        products = []
        for product in soup.find_all('a', class_='_link -pbxs'):
            product_info = {}
            product_info['id'] = product['id']
            product_info['name'] = product.find('h2', class_='product-name').text.strip()
            product_info['price'] = product.find('span', class_='product-price').text.strip()
            product_info['description'] = product.find('p', class_='product-description').text.strip()
            product_info['image'] = product.find('img')['src']
            products.append(product_info)
        print("products scraped is:", products)
        return(products)
    except Exception as e:
        print("Failed to fetch page:", e)
        return None

# Function to save data to CSV
def save_to_csv(data, filename):
    with open(filename, 'w', newline='') as csvfile:
        fieldnames = ['id', 'name', 'price', 'description', 'image']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for product in data:
            writer.writerow(product)

# Main function
def main():
    url = 'https://hairhaven.mt/product-category/brands/hair-care-brands/joico/'
    products = scrape_website(url)
    if products:
        save_to_csv(products, 'hair_products.csv')
        print("Data saved to hair_products.csv")
    else:
        print("No data scraped, products is: ", products)

if __name__ == "__main__":
    main()
