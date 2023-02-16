from datetime import date

class View:
    def message(self, message):
        print("-----------------------------------")
        print(f"{message}")
        print("-----------------------------------")

    def menu(self):
        print("1: Ajouter un joueur ")
        print("2: Liste de tous les joueurs ")
        print("3: Mettre à jour le classement d'un joueur ")
        print("4: Créer un tournoi ")
        print("5: Liste des tournois")
        print("6: Quittez l'application")
        print("-----------------------------------")

        try:
            user_choice = int(input("Entrez votre choix (1 - 6) :"))
            if user_choice > 0 and user_choice <= 6:
                return user_choice
            else:
                error_message = "Veuillez choisir un nombre compris dans la liste ⚠️"
                self.message(error_message)

        except ValueError:
            """ Except nous permet de gérer une erreur 
            ➡ Si l'utilisateur rentre d'autres caractères que des nombres"""
            error_message = "Veuillez choisir un nombre 🔢️"
            self.message(error_message)


    def new_player(self):
        last_name = input("Nom :")
        first_name = input("Prénom :")
        b_day = int(input("Jour de naissance : "))
        b_month = int(input("Mois de naissance :"))
        b_year = int(input("Année de naissance :"))
        dath_of_birth = date(b_year, b_month, b_day).strftime("%d/%m/%y")
        rank = int(input("Rang :"))
        return first_name, last_name, dath_of_birth, rank

    def display_player_list(self, list):
        for player in list:
            print(player)

    def modify_rank(self):
        last_name_player = input("Nom du joueur à modifier :")
        first_name_player = input("Nom du joueur à modifier :")
        rank = input("Nouveau classement :")
        return last_name_player, first_name_player, rank