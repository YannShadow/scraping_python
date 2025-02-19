# scraping_python
import requests
from bs4 import BeautifulSoup
import scrapy
#import pandas as pd
import csv

# definition de mon objet BS ETcrétion de la virable quote et finalisation de ma page cible 
Url_base = 'https://quotes.toscrape.com' #page cible


user_aget='Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36'

headers = {"User-Agent": user_aget}
# Faire une requête HTTP pour obtenir le HTML de la page
response = requests.get(Url_base, headers=headers)
soup = BeautifulSoup(response.text, 'html.parser')

# Trouver l'élément contenant la citation
quote_div = soup.find('div', class_='quote')


if quote_div:

    for quote_div in soup.find_all('div', class_='quote'):
        #quote_text = quote_div.find('span', class_='text').text.strip()
        author = quote_div.find('small', class_='author').text.strip()
       # tags = [tag.text.strip() for tag in quote_div.find_all('a', class_='tag')]
       # print(f"Citation: {quote_text}")
        print(f"Auteur: {author}")
       # print(f"Tags: {', '.join(tags)}")
        print()
        
        quote = {
            'Auteur': author,
        }

        # creation de mon fichier csv
        with open('quotes1.csv', 'a', newline='', encoding='utf-8') as csvfile:
            fieldnames = [ 'Auteur']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writerow(quote)

else:
    print("Aucune citation trouvée.")



