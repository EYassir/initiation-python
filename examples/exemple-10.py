def cap(chaine):
    if "." in chaine:
        phrases=chaine.split(".")
        liste_phrases=[]
        for phrase in phrases:
            liste_phrases.append(cap(phrase))
        return (".".join(liste_phrases))
    else:
        i=len(chaine)-len(chaine.lstrip()) # i= nombre d'espace à gauche
        return (" "*i)+chaine.lstrip().capitalize()

def write():
    f=open(filename,"a")
    while 1:
        line=input("Entrez une ligne : ")
        if line=="":
            break
        f.write(cap(line)+"\n")
    f.close()

def read():
    f=open(filename,"r")
    while 1:
        line=f.readline()
        if line=="":
            break
        print(line)
    f.close()

filename=input("nom du fichier : ")
choice=input("'w' pour ecrire, \n'r' pour lire \n=>> ")
if choice=="w":
    write()
else:
    read()
