from datetime import date

class View:

    def welcome(self, title):
        print("-----------------------------------")
        print(f"{title}")
        print("-----------------------------------")

    def menu(self):
        print("1: Ajouter un joueur ")
        print("2: Mettre à jour le classement d'un joueur  ")
        print("3: Créer un tournoi ")
        print("4: Liste de tous les joueurs ")
        print("5: Liste des tournois")
        print("6: Quittez l'application")
        print("-----------------------------------")

        try:
            user_choice = int(input("Entrez votre choix (1 - 6) :"))
            if user_choice > 0 and user_choice <= 6:
                return user_choice
            else:
                print("Veuillez choisir un nombre compris dans la liste !")
        except ValueError:
            """ Except nous permet de gérer une erreur 
            ➡ Si l'utilisateur rentre d'autres caractères que des nombres"""
            print("Veuillez choisir un nombre !")

    def newPlayer(self):
        first_name = input("Prénom :")
        last_name = input("Nom :")
        b_day = int(input("Jour de naissance : "))
        b_month = int(input("Mois de naissance :"))
        b_year = int(input("Année de naissance :"))
        dath_of_birth = date(b_year, b_month, b_day).strftime("%d/%m/%y")
        rank = int(input("Rang :"))
        return first_name, last_name, dath_of_birth, rank
