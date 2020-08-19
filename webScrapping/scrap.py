
import requests
from bs4 import BeautifulSoup
url="https://en.wikipedia.org/wiki/List_of_best-selling_fiction_authors"

response=requests.get(url)

if response.ok:
    soup = BeautifulSoup(response.text,"html.parser")
    table = soup.find("table",{"class":"wikitable"}) 
    tbody = table.find("tbody")
    trs = table.findAll("tr")
    for tr in trs:
        tds=tr.findAll("td")
        author={}
        if len(tds)>0:
            author["name"]=tds[0].find("a").text
            author["speciality"]=tds[4].text.replace('\n', '')
            print(author)
            