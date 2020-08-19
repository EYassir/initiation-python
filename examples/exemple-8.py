def factoriel(nombre):
    # iteration 1 : nombre=3
    # iteration 2 : nombre=2
    # iteration 3 : nombre=1
    #print("nombre en entré "+str(nombre))
    if nombre==1 or nombre==0:
        return 1
    else:
        #print("recursive : "+str(factoriel(nombre-1) ))
        return nombre * factoriel(nombre-1)

print(factoriel(3))
