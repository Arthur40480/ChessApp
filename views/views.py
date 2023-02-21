from datetime import date

class View:

    """ ----- ----- MENU ----- ----- """
    def message(self, message):
        print("-----------------------------------")
        print(f"{message}")
        print("-----------------------------------")

    def menu(self):
        print("1: Ajouter un joueur ")
        print("2: Liste des joueurs ")
        print("3: Créer un tournoi ")
        print("4: Liste des tournois")
        print("5: Quittez l'application")
        print("-----------------------------------")

        try:
            user_choice = int(input("Entrez votre choix (1 - 6) :"))
            if user_choice > 0 and user_choice <= 6:
                return user_choice
            else:
                error_message = "⚠️ Veuillez choisir un nombre compris dans la liste ⚠️"
                self.message(error_message)

        except ValueError:
            """ Except nous permet de gérer une erreur 
            ➡ Si l'utilisateur rentre d'autres caractères que des nombres"""
            error_message = "🔢️ Veuillez choisir un nombre 🔢️"
            self.message(error_message)


    """ ----- ----- JOUEUR ----- ----- """
    def new_player(self):
        last_name = input("Nom :")
        first_name = input("Prénom :")
        b_day = int(input("Jour de naissance : "))
        b_month = int(input("Mois de naissance :"))
        b_year = int(input("Année de naissance :"))
        dath_of_birth = date(b_year, b_month, b_day).strftime("%d/%m/%y")
        rank = int(input("Rang :"))
        return first_name, last_name, dath_of_birth, rank

    def display_player_list(self, players_list):
        for player in players_list:
            print(player)

    def modify_rank(self):
        last_name_player = input("Nom du joueur à modifier :")
        first_name_player = input("Prénom du joueur à modifier :")
        rank = input("Nouveau classement :")
        return last_name_player, first_name_player, rank

    """ ----- ----- TOURNOI ----- ----- """
    def new_tournament(self):
        name = input("Le nom du tournoi :")
        place = input("Où :")
        start_date = date(input("Date de début (dd/mm/yyyy) :")).strftime("%d/%m/%Y")
        end_date = date(input("Date de fin (dd/mm/yyyy) :")).strftime("%d/%m/%Y")
        round = input("Nombre de tours (4 par défaut) :" or "4")
        description = input("Remarques générales :")

    def tournament_roster(self, players):
        x = 0
        for player in players:
            x = x + 1
            print(str(x) + " " + "➡" + " " + player["last_name"] + " " + player["first_name"] + " " + str(player["rank"]) )
        print("-----------------------------------")

    def start_tournament(self):
        start_title = "🚥 Voulez vous commencer le tournoi ? 🚥"
        self.message(start_title)
        answer = input(" (Y/N) :")
        return  answer


    """ ----- ----- ROUND ----- ----- """
    def play_first_round(self, start_date):
       first_round_title = f" 🎌 Round 1  {start_date} 🎌"
       self.message(first_round_title)


    """ ----- ----- MATCH ----- ----- """
    def match_title(self, first_player, second_player):
        print(f"💥 Joueur 1 - {first_player} contre Joueur 2 - {second_player} 💥")

    def color_draw(self, first_player, second_player, color):
        print("🎲 Tirage au sort pour les couleurs ! 🎲")
        print("---------------------")
        print(f"Joueur 1: {first_player} jouera les {color[0]} !")
        print(f"Joueur 2: {second_player} jouera les {color[1]} !")
        print("---------------------")
        print("🔥 Le match commence ! 🔥")

    def match_result(self, first_player, second_player):
        print("📣 Fin du match ! 📣")
        print("---------------------")
        print("Résultat du match ?")
        print(f"1 - Joueur 1 - {first_player} vainqueur !")
        print(f"2 - Joueur 2 - {second_player} vainqueur !")
        print(f"3 - Egalité parfaite !")
        try:
            result = int(input("Veuillez entrer le résultat du match (1/2/3) :"))
            if result > 0 and result <= 3:
                return result
            else:
                error_message = "⚠️ Veuillez choisir un réultat correct ⚠️"
                self.message(error_message)
        except ValueError:
            error_message = "🔢️ Veuillez choisir un nombre (1/2/3) 🔢️"
            self.message(error_message)

    def end_match(self):
        input("🕦 Veuillez appuyer sur Entrer lorsque le match est terminer 🕦")



