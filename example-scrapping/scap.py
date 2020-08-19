from bs4 import BeautifulSoup
import requests

#Lancer une requette get vers l'url    
url ="https://en.wikipedia.org/wiki/List_of_best-selling_fiction_authors"
response = requests.get(url)

#si response et success 200
if response.ok:
    #récuperer le contenue html de la reponse et le parser avec beautifullsoup
    s = BeautifulSoup(response.text,"html.parser")
    #recuperer le tableau dans le contenu html recuperé
    table= s.find("table",{"class":"wikitable sortable"})
    #récuperer le body (contenue du tableau)
    tbody = table.find("tbody")
    #récuperer les lignes qui figurent dans le contenue du tableau
    table_rows=tbody.findAll("tr")
    for row in table_rows:
        author={}
        #recuperer les columns de la ligne 
        liste_column=row.findAll("td")
        if len(liste_column)>0:
            author["name"]=liste_column[0].find("a").text
            #author["name"]=liste_column[0].text.replace('\n','')
            author["specialisation"]=liste_column[4].text.replace('\n','')            
            #print(author)
            requests.post(" http://127.0.0.1:5000/authors",json=author)


    