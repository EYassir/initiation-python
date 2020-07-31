from datetime import date

class Personne(object):
    def __init__(self, nom, prenom, dateN):
        self.nom=nom
        self.prenom=prenom
        elm=dateN.split("/")
        print(elm)
        if len(elm)==3:
            self.daten=date(int(elm[2]),int(elm[1]),int(elm[0]))
        else:
            self.daten=date()

    def afficher(self):
        print ("Je m'appelle "+self.nom+" "+self.prenom+" et je suis ne le "+str(self.daten))

    def calculerAge(self):
        today = date.today()
        anniversaire = self.daten.replace(year=today.year)
        if anniversaire > today:
            return today.year - self.daten.year - 1
        else:
            return today.year - self.daten.year

personne1=Personne('dupond', 'david',"06/02/1980")
personne1.afficher()
print (personne1.calculerAge())