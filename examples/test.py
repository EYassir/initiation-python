# chaine=input("Qu'elle est la chaine à parcourir ?")
# caractere_a_trouver=input("Quel est le caractére à tourver ?")

# index=0
# found=False
# # Boucle while qui parcours la chaine de caractére 
# # Une condition valeur de l'index plus petit que la taille de la chaine
# # Une condition caractére trouvé (found) qui est fausse
# while(index<len(chaine) and not found):
#     #récupérer le caractére depuis la chaine à la position [index]
#     #comparer avec la caractére àa chercher
#     if chaine[index]==caractere_a_trouver:
#         print("premiere occurence touvé à la position (index) "+str(index))
#         #si identitique mettre la variable found en True
#         #pour sortir de la boucle lors du prochain passage
#         found=True
#     index+=1
# else:
#     print("final index "+str(index))

# # for caractere in chaine:
# #     if caractere_a_trouver==caractere and not found:
# #         print("premiere occurence touvé à la position (index) "+str(index))
# #         found=True
# #         break 
# #     index+=1

# # print("final index "+str(index))



# list_employ=[]

# emp1={
#     "nom":"joe",
#     "prenom":"doe",
#     "age":50,
#     "job":"developper"
# }
# list_employ.append(emp1)
# emp2={
#     "nom":"diana",
#     "prenom":"queen",
#     "age":50,
#     "job":"princesse"
# }

# list_employ.append(emp2)
# emp3={
#     "nom":"joe",
#     "prenom":"doe",
#     "age":20,
#     "job":"developper"
# }

# emp3.pop("age")

# print(emp3)

# list_employ.append(emp3)

# for emp in list_employ:
#     print(emp["nom"])
#     # if emp["nom"]=="joe":
#     #     print("yooo")


# import json

# # with open("todos.json") as json_file:
# #     data=json.load(json_file)
# #     for p in data: # select * from todos        
# #         if not p["completed"] and "tempora" in p["title"]: # where completed is false and title like %tempora%
# #             print(p)            

# with open("users.json") as json_file:
#     data=json.load(json_file)
#     #tous les employé de la company "Romaguera-Crona"
#     for p in data:
#         if "Romaguera-Crona" in p["company"]["name"]:                
#             print(p["name"])

class MonException(Exception):
	pass

try:
	raise MonException("Mon message d'erreur")
except MonException:
	print ("Le message d'erreur ")