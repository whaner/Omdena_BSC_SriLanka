import requests
from bs4 import BeautifulSoup
#import csv
import pandas as pd

# Base URL of the website to scrape
#base_url = "https://ceylontoday.lk/category/ceylon-today-sunday/news-ceylon-today-sunday/page/" #Ceylon Today – Sunday
base_url = "https://ceylontoday.lk/category/ceylon-today-daily/news/page/" #Ceylon Today – Sunday

# Initialize an empty list to store article data
articles_data = []
pagina = 0
# Iterate over the pages
for page in range(1, 1193):
    pagina = pagina+1
    print(pagina)
    url = f"{base_url}{page}/"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')


    # Find all article entries on the page
    articles = soup.find_all('h3', class_='entry-title td-module-title')
    for article in articles:
        link = article.find('a')['href']
        # Append the article details to the list
        articles_data.append(link)

df = pd.DataFrame(articles_data, columns=['url'])

# Save the DataFrame to a CSV file
df.to_csv('ceylon_today_daily_urls.csv', index=False, encoding='utf-8', sep=',')