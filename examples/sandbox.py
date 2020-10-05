Liste_hobbies = []
Liste_hobbies.append(
    {"Name": "Lecture", "Desc": "lire des livres", "Difficulté": 1})
Liste_hobbies.append(
    {"Name": "Netflix", "Desc": "voir des trucs", "Difficulté": 0})
Liste_hobbies.append(
    {"Name": "Natation", "Desc": "Faire comme les poisson", "Difficulté": 3})
Liste_hobbies.append(
    {"Name": "cuisine", "Desc": "Faire à manger", "Difficulté": 2})
Liste_hobbies.append(
    {"Name": "Bricolage", "Desc": "Faire des travaux", "Difficulté": 5})


hobbies = []
hobbies.append(Liste_hobbies[0])
hobbies.append(Liste_hobbies[1])
# Employees
bob = {
    "Name": "bob",
    "Age": 31,
    "hobbies": hobbies,
    "salary": 2000
}

alice = {
    "Name": "Alice",
    "Age": 40,
    "hobbies": [Liste_hobbies[0],
                {"Name": "Running",
                 "Desc": "courir",
                 "Difficulté": 1},
                Liste_hobbies[3]
                ],
    "salary": 2000
}

joe = {
    "Name": "Joe",
    "Age": 25,
    "hobbies": [Liste_hobbies[2],
                Liste_hobbies[4]
                ],
    "salary": 2000
}

# Les services

marketing = {
    "Name": "Marketing",
    "Description": "tchatch",
    "nbr_emp": 0,
    "emp": []
}

it = {
    "Name": "IT",
    "Description": "tech",
    "nbr_emp": 0,
    "emp": []
}

finance = {
    "Name": "Finance",
    "Description": "Money",
    "nbr_emp": 0,
    "emp": []
}

it["emp"].append(bob)
it["emp"].append(
    {
        "Name": "Victor",
        "Age": 23,
        "hobbies": [Liste_hobbies[3], Liste_hobbies[4]],
        "salary": 2000
    })
it["nbr_emp"] = len(it["emp"])  # Calcul nombre d'employe du service


marketing["emp"].append(alice)
marketing["emp"].append(
    {
        "Name": "Marry",
        "Age": 25,
        "hobbies": [Liste_hobbies[3], Liste_hobbies[4]],
        "salary": 2000
    })
marketing["nbr_emp"] = len(it["emp"])  # Calcul nombre d'employe du service

finance["emp"].append(joe)
finance["emp"].append(
    {
        "Name": "Kevin",
        "Age": 25,
        "hobbies": [Liste_hobbies[3], Liste_hobbies[4]],
        "salary": 2000
    })
finance["nbr_emp"] = len(it["emp"])  # Calcul nombre d'employe du service

Liste_service = [marketing, it, finance]


# for srv in Liste_service:
#     for emp in srv["emp"]:
#         print("Employé : "+emp["Name"])
#         print("Hobbies : ")
#         print(emp["hobbies"])
#         print("**************************")

joe["hobbies"].append({"Name": "surf"})

# Augmenter le salaire
for emp in it["emp"]:
    emp["salary"] += 1000
# reduire le salaire
for emp in finance["emp"]:
    emp["salary"] -= 500
for emp in marketing["emp"]:
    emp["salary"] -= 500

# Retirer Kevin et l'affecter au service marketing
kevin = {}
index = 0
for emp in finance["emp"]:
    if emp["Name"] == "Kevin":
        kevin = emp
        finance["emp"].pop(index)
        finance["nbr_emp"] = len(finance["emp"])
        marketing["emp"].append(kevin)
        marketing["nbr_emp"] = len(marketing["emp"])
        break
    index += 1


print("Marketing : ")
print(marketing["nbr_emp"])
print(marketing["emp"])

print("************************")

print("finance : ")
print(finance["nbr_emp"])
print(finance["emp"])

print("************************")

print("IT : ")
print(it["nbr_emp"])
print(it["emp"])
