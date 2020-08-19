filename="test1.txt"
def ecrire():
    with open(filename,"a") as file:
        while True:
            msg=input("Entrez votre message : ")
            if msg=="":
                break
            else:
                file.write(msg+"\n")
def lire():
    with open(filename,"r") as file:
        print(file.read())

def recherche(keyword):
    found={
        "line_where_exist":[],
        "nombre_occurence":0
    }
    with open(filename,"r") as file:        
        for line in file.readlines():
            if keyword in line:
                found["nombre_occurence"]+=1
                found["line_where_exist"].append(line)
    return found

while True:
    choice=input(" 'w' pour ercire\n 'r' pour lire\n 'f' pour rechercher un mot \n 'q' pour quitter\n >>>")
    if choice=="w":
        ecrire()
    elif choice=="r":
        lire()
    elif choice=="f":
        keyword=input("quel est le mot à rechercher : ")
        resultat=recherche(keyword)
        print("le mots à été trouvés "+str(resultat["nombre_occurence"]))
        print("Dans les lignes")
        for i in resultat["line_where_exist"]:
            print("ligne :  "+i+"\n")
        break
    else:
        break