def manipInt(*args):    
    liste2=[i for i in args if type(i)==int] #je boucle -> verifie si c'est int -> et j'affecte directement liste2
    if liste2==list(args):
        print('max : '+ str(max(liste2)))
        print('min : '+ str(min(liste2)))
        print('somme : '+str(sum(liste2)))
        print ('moyenne : '+str(sum(liste2)/float(len(liste2))))
    else:
        print("ce n'est pas une liste de int")
    return

def factorielle(n):
    i,factorielle=1,1
    while i<=n:
        #factorielle*=i
        factorielle=factorielle*i
        i+=1
    return factorielle

manipInt(1,3,5,6)

print ("Factorielle : "+str(factorielle(3)))