import requests
from bs4 import BeautifulSoup
import pandas as pd

data = pd.read_csv('ceylon_today_sunday_urls_sample.csv')

urls = data['url'].tolist()

# Function to scrape a single URL
def scrape_url(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    # Extracting the Title, Author, Date, and Content
    title = soup.find('h1', class_='entry-title').get_text(strip=True)
    #author = soup.find('div', class_='eltd-post-info-author-link').get_text(strip=True)
    #date = soup.find('time', class_='eltd-post-info-date entry-date updated').get_text(strip=True)
    #comments = soup.find('a', class_='eltd-post-info-comments').get_text(strip=True)
    #content = soup.find('p').get_text(strip=True)
    paragraphs = soup.find_all('p')
    content = ' '.join(p.get_text(strip=True) for p in paragraphs)

    return {
        #'url': url,
        'title': title,
        #'author': author.strip('author: '),
        #'#comments': comments.strip(' Comments'),
        #'Date': date,
        'Content': content
    }

# Main function to scrape all URLs
def main():
    results = []
    for url in urls:
        try:
            result = scrape_url(url)
            results.append(result)
        except Exception as e:
            print(f"Error scraping {url}: {e}")

    #print(results)
    # Print the results
    #for result in results:
    #    print(result)
    
    # Convertendo os resultados para um DataFrame do Pandas
    df = pd.DataFrame(results)

    # Exportando o DataFrame para um arquivo CSV
    df.to_csv('sample_results_ceylon_today.csv', index=False, encoding='utf-8')

    #print("Exportação para CSV concluída com Pandas.")

if __name__ == "__main__":
    main()



