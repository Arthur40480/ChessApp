from datetime import date

class View:

    """ ----- ----- MENU ----- ----- """
    def message(self, message):
        print("-----------------------------------")
        print(f"{message}")
        print("-----------------------------------")

    def menu(self):
        print("🙋 Ajouter un joueur ➡ 1 ")
        print("🏆 Créer un tournoi ➡ 2")
        print("📃 Afficher un rapport ➡ 3")
        print("❌ Quittez l'application ➡ 4")
        print("-----------------------------------")

        try:
            user_choice = int(input("Entrez votre choix (1 - 4) :"))
            if user_choice > 0 and user_choice <= 4:
                return user_choice
            else:
                error_message = "⚠️ Veuillez choisir un nombre compris dans la liste ⚠️"
                self.message(error_message)
                self.menu()

        except ValueError:
            """ Except nous permet de gérer une erreur 
            ➡ Si l'utilisateur rentre d'autres caractères que des nombres"""
            error_message = "🔢️ Veuillez choisir un nombre 🔢️"
            self.message(error_message)
            self.menu()

    def rapport_menu(self):
        print("🙋 Afficher tous les joueurs par ordre alphabétique ➡ 1 ")
        print("🏆 Afficher tous les tournois ➡ 2")
        print("🙆‍♀️ Afficher les joueurs d'un tournoi par ordre alphabétique ➡ 3")
        print("📚 Afficher la liste de tous les tours d'un tournoi ainsi que tous les matchs de chaque tour ➡ 4")
        print("❌ Retour à l'accueil ➡ 5")
        print("-----------------------------------")

        try:
            user_choice = int(input("Entrez votre choix (1 - 5) :"))
            if user_choice > 0 and user_choice <= 5:
                return user_choice
            else:
                error_message = "⚠️ Veuillez choisir un nombre compris dans la liste ⚠️"
                self.message(error_message)
                self.rapport_menu()

        except ValueError:
            """ Except nous permet de gérer une erreur 
            ➡ Si l'utilisateur rentre d'autres caractères que des nombres"""
            error_message = "🔢️ Veuillez choisir un nombre 🔢️"
            self.message(error_message)
            self.rapport_menu()

    def back_to_menu(self):
        print("-----------------------------------")
        answer = input("💒 Revenir à l'acceuil ? (Oui/Non): ")
        print("-----------------------------------")
        return answer



    """ ----- ----- JOUEUR ----- ----- """
    def new_player(self):
        last_name = input("Nom :")
        first_name = input("Prénom :")
        b_day = int(input("Jour de naissance : "))
        b_month = int(input("Mois de naissance :"))
        b_year = int(input("Année de naissance :"))
        dath_of_birth = date(b_year, b_month, b_day).strftime("%d/%m/%y")
        return first_name, last_name, dath_of_birth

    def player_list_title(self):
        list_title = " 📃 Liste des joueurs enregistrés 📃"
        self.message(list_title)

    def add_player_in_file_title(self):
        add_player_in_file_title = "🎉 Joueur bien enregistrer 🎉"
        self.message(add_player_in_file_title)

    def display_player_list(self, players_list):
        for player in players_list:
            last_name = player["last_name"]
            first_name = player["first_name"]
            age = player["dath_of_birth"]
            print(f"{last_name} {first_name}, date de naissance: {age}")

    def display_roster_list(self, tournament):
        tournament_name = tournament["name"]
        roster_list_title = f"📃 Voici les joueurs participants au tournoi: {tournament_name} 📃"
        self.message(roster_list_title)
        roster_list = tournament["players_list"]
        for player in roster_list:
            last_name = player["last_name"]
            first_name = player["first_name"]
            age = player["dath_of_birth"]
            print(f"{last_name} {first_name}, date de naissance: {age}")




    """ ----- ----- TOURNOI ----- ----- """
    def new_tournament_title(self):
        tournament_creation_title = "🏁 Création d'un nouveau tournoi 🏁"
        self.message(tournament_creation_title)

    def new_tournament(self):
        name = input("Le nom du tournoi :")
        place = input("Où :")
        start_date_d = int(input("Jour de début (dd) :"))
        start_date_m = int(input("Mois de début (mm) :"))
        start_date_y = int(input("Année de début (yyyy) :"))
        end_date_d = int(input("Jour de fin (dd) :"))
        end_date_m = int(input("Mois de fin (mm) :"))
        end_date_y = int(input("Année de fin (yyyy) :"))
        round = int(input("Nombre de tours (4 par défaut) :" or 4))
        current_round = int(input("Numéro du tour actuel :" or 1))
        description = input("Remarques générales :")
        return name, place, start_date_d, start_date_m, start_date_y, end_date_d, end_date_m, end_date_y, round, current_round, description

    def tournament_roster_title(self):
        roster_title = "🏆 Veuillez choisir les joueurs participants au tournoi (8 joueurs max) 🏆"
        self.message(roster_title)

    def select_error_list(self):
        error_title = "❗ Ceci n'est pas un numéro, veuillez ajouter un numéro ❗"
        self.message(error_title)

    def tournament_roster(self, players):
        x = 0
        for player in players:
            x = x + 1
            print(str(x) + " " + "➡" + " " + player["last_name"] + " " + player["first_name"])
        print("-----------------------------------")

    def add_tournament_in_file_title(self):
        add_tournament_in_file_title = "🎉 Tournoi bien enregistrer 🎉"
        self.message(add_tournament_in_file_title)

    def start_tournament(self):
        start_title = "🚥 Voulez vous commencer le tournoi ? 🚥"
        self.message(start_title)
        answer = input(" (Oui/Non) :")
        return  answer

    def tournament_list_title(self):
        list_title = " 📃 Liste des tournois 📃"
        self.message(list_title)

    def display_tournament_list(self, tournament_list):
        x = 0
        for tournament in tournament_list:
            x = x + 1
            name = tournament["name"]
            place = tournament["place"]
            start_date = tournament["start_date"]
            end_date = tournament["end_date"]
            print(f"{x}. ➡ Nom du tournoi: {name}, Lieu: {place}, date de début: {start_date}, date de fin: {end_date}")
        print("-----------------------------------")




    """ ----- ----- ROUND ----- ----- """
    def play_first_round(self, start_date):
       first_round_title = f" 🎌 Round 1  {start_date} 🎌"
       self.message(first_round_title)

    def ask_next_round_title(self, current_round):
        ask_next_round = f"🎌 Voulez vous lancer le Round {current_round} ? 🎌"
        self.message(ask_next_round)
        answer = input("(Oui/Non) :")
        return answer



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






