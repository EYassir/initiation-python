from datetime import datetime
a=datetime.now()
hour=a.hour
print(" Example 1 \n")
nom=input(" Veuillez saisir le nom : ")
genre=input(" Veuillez saisir le genre 0 pour homme ou 1 pour femme : ")
age=input(" Veuillez saisir l'age : ")

if genre=='0':
    genre="un homme"
else:
    genre="une femme"
greeting=""
if int(hour)>17:
    greeting="Bonsoir"
else:
    greeting="Bonjour"

print(greeting+" "+nom+" vous etes "+genre+" agé de "+age+ " ans")