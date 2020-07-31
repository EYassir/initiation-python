
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

print(cap("test,test0"))
print(cap("test. test1"))
