from views.views import View
from models.player import Player
from models.tournament import Tournament
from models.tour import Tour
from tinydb import TinyDB, Query, where
from datetime import datetime
from datetime import date
import random

class Controller:

    """ ----- ----- Menu ----- ----- """
    def __init__(self):
        """ Initialise les valeurs du Conbtroller via le constructeur __init__ """
        self.db = TinyDB("data/players/db.json")
        self.players_table = self.db.table("Players")
        self.db_tournament = TinyDB(f"data/tournaments/db.json")
        self.tournament_table = self.db_tournament.table(f"Tournaments")
        self.view = View()
        self.user = Query()

    def display_menu(self):
        """ Fait apparaître le menu """
        welcom_title = "♟️ Bienvenue dans l'application de tournois d'echecs ♟️"
        self.view.message(welcom_title)
        user_choice = self.view.menu()
        if user_choice == 1:
            self.new_player()
        if user_choice == 2:
            self.new_tournament()
        if user_choice == 3:
            self.display_rapport_menu_title()
        if user_choice == 4:
            exit()

    def display_rapport_menu_title(self):
        """ Fait apparaître le titre """
        rapport_title = "📃 Menu des rapports 📃"
        self.view.message(rapport_title)
        self.display_menu_rapport()

    def display_menu_rapport(self):
        """ Fait apparaître le menu des rapports """
        user_choice = self.view.rapport_menu()
        if user_choice == 1:
            self.display_player_list()
        if user_choice == 2:
            self.display_tournament_list()
        if user_choice == 3:
            self.display_roster_list()
        if user_choice == 4:
            exit()
        if user_choice == 5:
            self.display_menu()

    def back_to_menu(self):
        """ Permet de revenir au menu principal """
        answer = self.view.back_to_menu()
        if (answer == "N" or answer == "Non" or answer == "non"):
            exit()
        else:
            self.display_menu()




    """ ----- ----- Joueur ----- ----- """
    def new_player(self):
        """ Créer un nouveau Joueur """
        player_creation_title = "🙋 Création d'un nouveau joueur 🙋"
        self.view.message(player_creation_title)
        data_player = self.view.new_player()
        first_name = data_player[0]
        last_name = data_player[1]
        dath_of_birth = data_player[2]
        chess_id = data_player[3]


        """ On viens vérifier si le joueur n'existe pas déjà """
        same_name = self.players_table.search(self.user.first_name == first_name)
        same_last_name = self.players_table.search(self.user.last_name == last_name)
        if same_last_name and same_name:
            error_message = "⚠️ Ce joueur est déjà enregistrer ⚠️"
            self.view.message(error_message)
            self.display_menu()

        player = Player(last_name, first_name, dath_of_birth, chess_id)
        self.add_player_in_file(player.__dict__)
        new_player_again = input("🔄 Voulez vous enregistrer un autre joueur ? 🔄 (Oui/Non) :")
        if (new_player_again == "O" or new_player_again == "Oui" or new_player_again == "oui"):
            self.new_player()
        else:
            self.display_menu()

    def players_roster(self):
        """ Création d'une liste contenant les joueurs enregistrés """
        players = self.players_table.all()
        players = sorted(players, key=lambda player: player['last_name'])
        player_roster = []
        for people in players:
            player = Player(
                people["last_name"],
                people["first_name"],
                people["dath_of_birth"],
                people["chess_id"]
            ).__dict__
            player_roster.append(player)
        return player_roster

    def add_player_in_file(self, data):
        """ Enregistre le joueur dans le fichier JSON """
        self.players_table.insert(data)
        self.view.add_player_in_file_title()

    def display_player_list(self):
        """ Affiche la liste des joueurs enregistrer par ordre alphabétique (Nom) """
        self.view.player_list_title()
        players = sorted(self.players_table, key=lambda player: player['last_name'])
        self.view.display_player_list(players)
        self.back_to_menu()

    def display_roster_list(self):
        """ Affiche les joueurs participant au tournoi séléctionner """
        tournament = self.tournament_list()
        self.view.display_tournament_list(tournament)
        tournament_select = int(input("Veuillez ajouter le numéro du tournoi:"))
        tournament_select = tournament_select - 1
        self.view.display_roster_list(tournament[tournament_select])
        self.back_to_menu()




    """ ----- ----- TOURNOI ----- ----- """
    def new_tournament(self):
        """ Créer un Tournoi """
        self.view.new_tournament_title()
        tournament_data = self.view.new_tournament()
        name = tournament_data[0]
        place = tournament_data[1]
        start_date = date(tournament_data[4], tournament_data[3], tournament_data[2]).strftime("%d/%m/%y")
        end_date = date(tournament_data[7], tournament_data[6], tournament_data[5]).strftime("%d/%m/%y")
        round = tournament_data[8]
        current_round = tournament_data[9]
        description = tournament_data[10]
        roster_list = self.tournament_roster()
        round_list = []
        tournament = Tournament(
            name,
            place,
            start_date,
            end_date,
            description,
            roster_list,
            round_list,
            round,
            current_round,
        )
        self.add_tournament_in_file(tournament.__dict__)
        self.start_tournament(tournament.__dict__)

    def add_tournament_in_file(self, data):
        """ Enregistre le tournoi dans le fichier JSON """
        self.tournament_table.insert(data)
        self.view.add_tournament_in_file_title()

    def tournament_roster(self):
        """ Permet la séléction des joueurs participant au tournoi """
        self.view.tournament_roster_title()
        roster_list = []
        players = self.players_roster()
        self.view.tournament_roster(players)
        while len(roster_list) < 8:
            try:
                number_select = int(input("Veuillez ajouter le numéro du joueur séléctionner:"))
                if number_select > 0 and number_select <= len(players):
                    player_select = (number_select - 1)
                    roster_list.append(players[player_select])
                else:
                    print(f"😓 Le joueur numéro {number_select} n'éxiste pas ! 😓")
            except ValueError:
                self.view.select_error_list()
        return roster_list


    def start_tournament(self, tournament):
        """ Lance le tournoi """
        answer = self.view.start_tournament()
        if (answer == "O" or answer == "Oui" or answer == "oui"):
            self.play_first_round(tournament)
        else:
            self.display_menu()

    def display_tournament_list(self):
        """ Affiche la liste des tous les tournois """
        self.view.tournament_list_title()
        tournament = self.tournament_table
        self.view.display_tournament_list(tournament)
        self.back_to_menu()

    def tournament_list(self):
        """ Créer une liste de tous les tournois enregistrés """
        tournament_table = self.tournament_table
        tournament_list = []
        for tournament in tournament_table:
            tournaments = Tournament(
                tournament["name"],
                tournament["place"],
                tournament["start_date"],
                tournament["end_date"],
                tournament["description"],
                tournament["players_list"],
                tournament["round_list"],
                tournament["nbr_rounds"],
                tournament["current_round"],
            ).__dict__
            tournament_list.append(tournaments)
        return tournament_list


    """ ----- ----- ROUND ----- ----- """
    def play_first_round(self, tournament):
        """ Annonce le premier Round """
        roster_list = tournament["players_list"]
        start_date = datetime.today().strftime('%d/%m/%Y-%H:%M:%S')
        self.view.play_first_round(start_date)

        """ On définit les matchs """
        match_list = self.mix_player(roster_list)
        result_match_list = []
        for match in match_list:
            """ Pour chaques match dans la liste, on viens chercher le résultat, et on l'ajoute à la liste de résultat """
            result_match_list.append(self.play_match(match))
        end_date = datetime.today().strftime('%d/%m/%Y-%H:%M:%S')

        """ Annonce de la fin du premier Round """
        end_first_round = f"🎌 Fin du Round 1 - {end_date} 🎌"
        self.view.message(end_first_round)

        """ On viens mettre à jour le round actuel, on enregistre le round dans la liste de round du tournoi """
        self.update_tournament_file(1, start_date, end_date, result_match_list, tournament)

        """ On créer une liste qui vas contenir l'ensemble des matchs du tournoi """
        list_of_all_matchs = []
        for match_list in result_match_list:
            for match in match_list:
                list_of_all_matchs.append(match)
        self.ask_next_round(tournament, list_of_all_matchs, result_match_list)

    def play_others_rounds(self, list_of_all_matchs, result_match_list):
        """ Définit les matchs, et évite de retomber sur le même joueur """
        sorted_match_list = sorted(list_of_all_matchs, key=lambda player: player[1], reverse=True)
        match_list = []
        while len(sorted_match_list) != 0:
            i = 1
            player1 = sorted_match_list[0]
            player2 = sorted_match_list[i]
            match_1 = (player1, player2)
            match_verify = (player2, player1)

            if match_1 not in result_match_list and match_verify not in result_match_list:
                match_list.append(match_1)
                del sorted_match_list[i]
                del sorted_match_list[0]

            else:
                print("Le match à déjà été jouer")
                i += i
                for n in range(len(sorted_match_list)):
                    match_1 = (sorted_match_list[0], sorted_match_list[i])
                    match_verify = (sorted_match_list[i], sorted_match_list[0])
                    if match_1 not in result_match_list and match_verify not in result_match_list:
                        match_list.append(match_1)
                        del sorted_match_list[i]
                        del sorted_match_list[0]
                        print(sorted_match_list)
                        break
                    else:
                        i += 1
        return match_list

    def ask_next_round(self, tournament, list_of_all_matchs, result_match_list):
        """ Demande si on lance le round suivant """
        current_tournament = self.tournament_table.get(self.user.name == tournament["name"])
        next_round = current_tournament["current_round"]
        answer = self.view.ask_next_round_title(next_round)
        if (answer == "O" or answer == "Oui" or answer == "oui"):
            self.play_others_rounds(list_of_all_matchs, result_match_list)
        else:
            self.display_menu()

    def mix_player(self, roster_list):
        """ Mélange les joueurs, et définit les matchs (joueur vs joueur) sous forme de liste """
        random.shuffle(roster_list)
        size = 2
        sub_list = [roster_list[x: x + size] for x in range(0, len(roster_list), size)]
        return sub_list

    def update_tournament_file(self, current_round, start_date, end_date, match_list, tournament):
        """ Enregistre les nouvelles données dans le fichier JSON """
        name = tournament["name"]
        round = Tour(
            f"Round {current_round}",
            start_date,
            end_date,
            match_list
        )
        self.tournament_table.upsert({"name": name, "current_round": 2}, self.user.name == name)
        self.tournament_table.upsert({"name": name, "round_list": round.__dict__}, self.user.name == name)



    """ ----- ----- MATCHS ----- ----- """
    def play_match(self, match_list):
        """ Lance les matchs entre joueurs """
        first_player = match_list[0]["last_name"] + " " + match_list[0]["first_name"]
        second_player = match_list[1]["last_name"] + " " + match_list[1]["first_name"]
        first_player_score = 0
        second_player_score = 0
        self.view.match_title(first_player, second_player)
        self.color_draw(first_player, second_player)
        self.view.end_match()
        result = self.view.match_result(first_player, second_player)
        if result == 1:
            first_player_score = 1
        if result == 2:
            second_player_score = 1
        if result == 3:
            first_player_score = 0.5
            second_player_score = 0.5
        match_result = (
            [match_list[0], first_player_score],
            [match_list[1], second_player_score],
        )
        return match_result

    def color_draw(self, first_player, second_player):
        """ Assignation des couleurs aléatoirement """
        color = ["Blanc ⚪", "Noir ⚫"]
        random.shuffle(color)
        self.view.color_draw(first_player, second_player, color)




















