depenses = []
stock={
    'vetement':3000,'transport':2000,'alimentation':1000
}

def afficher_menu():
    print("\n --Gestion de Depense--")
    print("1. Ajouter une dépense par catégorie")
    print("2. Afficher les dépenses")
    print("3. Quitter")


def add_categorie(depenses):
    for i in range(1, 4):
        while True:
            categorie_input = (input(f"Categorie du produit {i} : "))
            if categorie_input.replace(' ','').isalpha():
                if categorie_input:
                    break
                else:
                    print("veuillez bien saisir.")
        while True:
            prix_categorie = input(f"Prix (en FcF)  : ")
            if prix_categorie.replace('.', '', 1).isdigit() and prix_categorie.count('.') <= 1 :
                prix_categorie = float(prix_categorie)
                if prix_categorie >= 0:
                    break
                else:
                    print("Prix incorrect, veuillez resaisir !")
            else:
                print("Prix invalide, veuillez entrer un nombre valide.") 
        while True:
            description = str(input("Décris le : "))
            if description.replace(' ','').isalpha():
                break
            else:
                print("Veuillez une description correct de votre depense")

        depenses.append({"categorie": categorie_input, "montant": prix_categorie})
    print("Dépenses par catégorie ajoutées")


def afficher_depenses(depenses):
    if not depenses:
        print("Aucune dépense enregistrée.")
        return
    print("\n----- Liste de toutes les dépenses : -----")
    total = 0
    categories = {}
    for i, depense in enumerate(depenses,1):
        prix_categorie = depense.get("montant")
        total += prix_categorie
        if "description" in depense:
            print(f"{i}. {depense['description']} : {prix_categorie} Fcf")
        elif "categorie" in depense:
            categorie = depense["categorie"]
            print(f"{i}. Catégorie { categorie} : {prix_categorie} Fcf")
            if  categorie not in categories:
                categories[ categorie] = 0
            categories[ categorie] += prix_categorie
            print("===========================================")
    
    print(f"\nTotal des dépenses : {total} Fcf")
    
    if categories:
        print("\n-----Dépenses par catégorie : -----")
        for  categorie, somme in categories.items():
            print(f"- { categorie} : {somme} Fcf")


# Boucle principale
while True:
    afficher_menu()
    while True:
        try:
            choix = int(input("Choisissez une option entre (1-3) : "))
            if 1 <= choix <= 3:
                break
            else:
                print("Choix invalide, veuillez choisir entre 1 et 3.")
        except ValueError:
            print("Veuillez entrer un nombre valide.")

    if choix == 1:
        add_categorie(depenses)
    elif choix == 2:
        afficher_depenses(depenses)
    elif choix == 3:
        print("Au revoir !")
        break