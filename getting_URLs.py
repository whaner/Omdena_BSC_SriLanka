import requests
from bs4 import BeautifulSoup
import csv

# Base URL of the website to scrape
base_url = "https://www.colombotelegraph.com/index.php/category/news/page/"

# Open a CSV file to write the articles to
with open('articles.csv', mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    # Write the header row
    writer.writerow(['Title', 'Date', 'URL'])

    # Iterate over the first 70 pages
    for page in range(1, 71):
        url = f"{base_url}{page}/"
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')

        # Find all article entries on the page
        articles = soup.find_all('div', class_='eltd-column1 eltd-content-left-from-sidebar')

        for article in articles:
            # Extract title, date, and URL
            #title_tag = article.find('h3', class_='eltd-pt-title')
            #title = title_tag.get_text(strip=True)
            #date = article.find('div', class_='eltd-pt-info-section').get_text(strip=True)
            #link = title_tag.find('a')['href']
            
            title = soup.find('h1', class_='eltd-post-title').get_text(strip=True)
            #author = soup.find('a', class_='eltd-post-info-author-link').get_text(strip=True)
            date = soup.find('time', class_='eltd-post-info-date entry-date updated').get_text(strip=True)
            #comments = soup.find('a', class_='eltd-post-info-comments').get_text(strip=True)
            #content = soup.find('div', class_='pf-content').get_text(strip=True)

            # Write the article details to the CSV file
            writer.writerow([title, date])

print("Scraping completed and data saved to articles.csv")
