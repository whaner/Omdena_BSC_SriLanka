import requests
from bs4 import BeautifulSoup

# List of URLs to scrape
urls = [
    "https://www.colombotelegraph.com/index.php/jaffna-university-teachers-association-condemns-police-violence-against-students-protestors-in-kilinochchi-on-the-independence-day/",
    "https://www.colombotelegraph.com/index.php/take-immediate-steps-to-repeal-online-safety-act-cpa/",
    "https://www.colombotelegraph.com/index.php/online-safety-act-major-blow-to-freedom-of-expression-amnesty-international/",
    "https://www.colombotelegraph.com/index.php/wickremesinghe-govt-continues-to-repress-freedoms-of-expression-pursue-policies-against-minorities-hrw/"
]

# Function to scrape a single URL
def scrape_url(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    # Extracting the Title, Author, Date, and Content
    title = soup.find('h1', class_='entry-title').get_text(strip=True)
    author = soup.find('a', class_='author-link').get_text(strip=True)
    date = soup.find('time', class_='published').get_text(strip=True)
    content = soup.find('div', class_='article-content').get_text(strip=True)

    return {
        'URL': url,
        'Title': title,
        'Author': author,
        'Date': date,
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

    # Print the results
    for result in results:
        print(result)

if __name__ == "__main__":
    main()
