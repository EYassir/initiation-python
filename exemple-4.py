ch = input("Entrez la chaine à traiter :")
car = input("Entrez le caractre à trouver :")

if ch=="" or car=="":
    print("veuillez saisir les infos demandés")
    exit()

found=False
i=0
while i<len(ch):
    if ch[i]==car:
        print(i)
        found=True
        break
    i=i+1

if not found:
    print("-1")

