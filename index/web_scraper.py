import requests
from bs4 import BeautifulSoup

def scrape_quotes():
    try:
        url = "http://quotes.toscrape.com"
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        quotes = soup.find_all('span', class_='text')
        for quote in quotes:
            print(quote.get_text())
    except requests.RequestException as e:
        print(f"Error: The webpage \"{url}\" was not accessible.")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    scrape_quotes()