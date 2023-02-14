""" Dictionnaire représentant le menu de l'application """
menu = {
    1: "➡️ Ajoutez un nouveau joueur",
    2: "➡️ Mettre à jour le classement d'un joueur",
    3: "➡️ Créez un nouveau tournoi",
    4: "➡️ Liste de tous les joueurs par ordre alphabétique",
    5: "➡️ Liste de tous les tournois",
    6: "➡️ Quittez l'application"
}


def lancement_de_lapplication():
    """Fonction qui permet de lancer l'application, et de récupérer le choix de l'utilisateur"""
    print("------------------")
    print("Bienvenue dans l'application CHAMPION CHESS ♟️")
    print("------------------")
    for numero, choix in menu.items():
        print(str(numero) + ":" + choix)
    print("------------------")
    option = input("Entrez votre choix :")
    choix_utilisateur(option)

def choix_utilisateur(option):
    """Fonction qui récupère la réponse, et apelle d'autre fonction suivant l'option choisit"""
    try:
        option = int(option)

    except Exception:
        """ Except nous permet de gérer une erreur ➡ Si l'utilisateur rentre d'autres caractères que des nombres"""
        option = str(option)
        print("Le choix de l'option est incorrect. Entrez un nombre entre 1 et 6. Merci.")
        lancement_de_lapplication()

    if option == 1:
        pass
    elif option == 2:
        pass
    elif option == 3:
        pass
    elif option == 4:
        pass
    elif option == 5:
        pass
    elif option == 6:
        print("Merci d'avoir utiliser CHAMPION CHESS ♟️")
        exit()
    else:
        print("Le choix de l'option est incorrect. Entrez un nombre entre 1 et 6. Merci.")
        lancement_de_lapplication()


lancement_de_lapplication()