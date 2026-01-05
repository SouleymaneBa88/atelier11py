depenses = []

def afficher_menu():
    print("\n --Gestion de depense--")
    print("1. Ajouter une description ")
    print("2. Ajouter une dépense par catégorie")
    print("3. Afficher les dépenses")
    print("4. Quitter")


def message(depenses):
    while True:
        description = str(input("Décris tes dépenses : "))
        if description.isalpha():
            print("cool")
            break
        else:
            print("Veuillez une description correct de votre depense")

    # while True:
    #     montant_str = input("Montant : ")
    #     if montant_str.replace('.', '', 1).isdigit():
    #         montant = float(montant_str)
    #         if montant >= 0:
    #             print("Montant bien saisi")
    #             break
    #         else:
    #             print("Montant incorrect, veuillez resaisir !")
    #     else:
    depenses.append({"description": description})
    print("Dépense bien ajoutée")


def categorie(depenses):
    for i in range(1, 4):
        while True:
            categorie_input = str(input(f"Type de produit {i} : "))
            if categorie_input.isalpha():
                break
            else:
                print("Le type de produit ne peut pas être vide.")
        while True:
            prix_categorie = input(f"Prix pour {categorie_input} : ")
            if prix_categorie.replace('.', '', 1).isdigit() and prix_categorie.count('.') <= 1:
                prix_categorie = float(prix_categorie)
                if prix_categorie >= 0:
                    break
                else:
                    print("Prix incorrect, veuillez resaisir !")
            else:
                print("Prix invalide, veuillez entrer un nombre valide.")
        depenses.append({"categorie": categorie_input, "montant": prix_categorie})
    print("Dépenses par catégorie ajoutées")


def afficher_depenses(depenses):
    if not depenses:
        print("Aucune dépense enregistrée.")
        return
    
    print("\nListe de toutes les dépenses :")
    total = 0
    categories = {}
    for i, dep in enumerate(depenses, 1):
        prix_categorie = dep.get("montant", 0)
        total += prix_categorie
        if "description" in dep:
            print(f"{i}. {dep['description']} : {prix_categorie} Fcf")
        elif "categorie" in dep:
            cate = dep["categorie"]
            print(f"{i}. Catégorie {cate} : {prix_categorie} Fcf")
            if cate not in categories:
                categories[cate] = 0
            categories[cate] += prix_categorie
    
    print(f"\nTotal des dépenses : {total} Fcf")
    
    if categories:
        print("\nDépenses par catégorie :")
        for cate, somme in categories.items():
            print(f"- {cate} : {somme} Fcf")


# Boucle principale
while True:
    afficher_menu()
    while True:
        try:
            choix = int(input("Choisissez une option (1-4) : "))
            if 1 <= choix <= 4:
                break
            else:
                print("Choix invalide, veuillez choisir entre 1 et 4.")
        except ValueError:
            print("Veuillez entrer un nombre valide.")
    if choix == 1:
        message(depenses)
    elif choix == 2:
        categorie(depenses)
    elif choix == 3:
        afficher_depenses(depenses)
    elif choix == 4:
        print("Au revoir !")
        break