from bs4 import BeautifulSoup
import requests


url ="https://www.amazon.fr/s?k=livres&page=2&__mk_fr_FR=%C3%85M%C3%85%C5%BD%C3%95%C3%91&qid=1597752368&ref=sr_pg_"

response = requests.get("https://www.amazon.fr/s?k=livres&page=2&__mk_fr_FR=%C3%85M%C3%85%C5%BD%C3%95%C3%91&qid=1597752368&ref=sr_pg_2")

print(response)
total_page=20

if response.ok:
    soup = BeautifulSoup(response.content)
    print(soup)