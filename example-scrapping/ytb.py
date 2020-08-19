from bs4 import BeautifulSoup
import requests

url ="https://www.youtube.com/"
response = requests.get(url)
if response.ok:    
    soup=BeautifulSoup(response.text,"html.parser")
    content = soup.find("ytd-app")
    print(content.find("div",{"id":"contents"}))
    # with open('output.txt', 'w',encoding="utf-8") as file:
    #     file.write(content)
    