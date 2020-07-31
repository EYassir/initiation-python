class STR(str):
    def __init__ (self,var):
        str.__init__(var)
    def cap(self):
        if '.' in self:
            phrases=self.split('.')
            liste_des_phrases=[]
            for phrase in phrases:
                phrase=STR(phrase)
                liste_des_phrases.append(phrase.cap())
            return STR(('. ').join(liste_des_phrases))
        else:
            chaine=self.strip()
            return STR(chaine[0].upper()+chaine[1:].lower())

    def iscap(self):
        if self.cap()==self:
            return True
        else: return False

    def __add__(self,autre):
        print ('addition')
        return STR(str.__add__(self,autre.cap()))


if __name__=='__main__':
    var=STR('Chaine. Test ok')
    print (var.cap())
    print (var.iscap())
    print ('\n')
    var2=STR('tse')
    print (var+var2)