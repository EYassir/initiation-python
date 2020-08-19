from bs4 import BeautifulSoup
import requests

url ="https://www.indeed.fr/jobs?q=data+scientist&l=Paris+%2875%29"
response = requests.get(url)
#print(response)
if response.ok:
    soup=BeautifulSoup(response.content,"html.parser")
    jobs=soup.findAll("div",{"class":"jobsearch-SerpJobCard"})
    for job in jobs:
        title=job.find("h2",{"class":"title"})
        location = job.find("div",{"class":"location"})
        if location==None:
            location = job.find("span",{"class":"location"})
        print(title.text)
        print(location.text)
        print("-------------------")
