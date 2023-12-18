from bs4 import BeautifulSoup as bs
import requests

def get_currency(in_curr, out_curr):
    url = f"https://www.x-rates.com/calculator/?from={in_curr}&to={out_curr}&amount=1"
    
    content = requests.get(url).text
    soup = bs(content, 'html.parser')
    currency = soup.find("span", class_="ccOutputRslt").get_text()

    return currency

print(get_currency("EUR", "USD"))