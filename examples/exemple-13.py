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
        try:
            anniversaire = self.daten.replace(year=today.year)
            print("in try")
        except ValueError: # erreur si personne est nee le 29 fev et l'annee courante n'est pas bissextile
            anniversaire = self.daten.replace(year=today.year, day=self.daten.day-1)
            print("in except")
        if anniversaire > today:
            return today.year - self.daten.year - 1
        else:
            return today.year - self.daten.year
    
    def saluer(self, autre):
        print (self.nom+" : Bonjour "+autre.nom)


personne1=Personne('dupond', 'david',"29/02/1988")
print (personne1.calculerAge())