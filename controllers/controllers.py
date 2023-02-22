from views.views import View
from models.player import Player
from tinydb import TinyDB, Query, where
from datetime import datetime
import random

class Controller:

    """ ----- ----- Menu ----- ----- """
    def __init__(self):
        """ Initialise les valeurs du Conbtroller via le constructeur __init__ """
        self.players_list = []
        self.db = TinyDB("data/players/db.json")
        self.players_table = self.db.table("Players")
        self.view = View()
        self.user = Query()

    def display_title(self):
        """ Fait apparaître le titre """
        welcom_title = "Bienvenue dans l'application de tournois d'echecs ♟️"
        self.view.message(welcom_title)
        self.display_menu()

    def display_menu(self):
        """ Fait apparaître le menu """
        user_choice = self.view.menu()
        if user_choice == 1:
            self.new_player()
        if user_choice == 2:
            self.display_player_list()
        if user_choice == 3:
            self.tournament_roster()



    """ ----- ----- Joueur ----- ----- """
    def new_player(self):
        """ Créer un nouveau Joueur """
        player_creation_title = "🙋 Création d'un nouveau joueur 🙋"
        self.view.message(player_creation_title)
        data_player = self.view.new_player()
        first_name = data_player[0]
        last_name = data_player[1]
        dath_of_birth = data_player[2]


        """ On viens vérifier si le joueur n'existe pas déjà """
        same_name = self.players_table.search(self.user.first_name == first_name)
        same_last_name = self.players_table.search(self.user.last_name == last_name)
        if same_last_name and same_name:
            error_message = "⚠️ Ce joueur est déjà enregistrer ⚠️"
            self.view.message(error_message)
            self.display_menu()

        player = Player(last_name, first_name, dath_of_birth, total_score=0)
        self.add_player_in_file(player.__dict__)
        new_player_again = input("🔄 Voulez vous enregistrer un autre joueur ? 🔄 (Y/N) :")
        if (new_player_again == "Y" or new_player_again == "Yes" or new_player_again == "yes"):
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
                people["total_score"],
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



    """ ----- ----- TOURNOI ----- ----- """
    def new_tournament(self):
        """ Créer un Tournoi """
        self.view.new_tournament_title()
        tournament_data = self.view.new_tournament()
        name = tournament_data[0]
        place = tournament_data[1]
        start_date = tournament_data[2]
        end_date = tournament_data[3]
        round = tournament_data[4]
        description = tournament_data[5]
        self.db_tournament = TinyDB(f"data/tournaments/{name}.json")
        self.tournament_table = self.db_tournament.table(f"{name}")

    def tournament_roster(self):
        """ Permet la séléction des joueurs participant au tournoi """
        self.view.tournament_roster_title()
        roster_list = []
        players = self.players_roster()
        self.view.tournament_roster(players)
        while len(roster_list) < 8:
            try:
                number_select = int(input("Veuillez ajouter le numéro du joueur séléctionner :"))
                if number_select > 0 and number_select <= len(players):
                    player_select = (number_select - 1)
                    roster_list.append(players[player_select])
                else:
                    print(f"😓 Le joueur numéro {number_select} n'éxiste pas ! 😓")
            except ValueError:
                self.view.select_error_list()
        self.start_tournament(roster_list)

    def start_tournament(self, roster_list):
        """ Lance le tournoi """
        answer = self.view.start_tournament()
        if (answer == "Y" or answer == "Yes" or answer == "yes"):
            self.play_first_round(roster_list)
        else:
            self.display_menu()



    """ ----- ----- ROUND ----- ----- """
    def play_first_round(self, roster_list):
        """ Lance le premier round """
        start_date = datetime.today().strftime('%d/%m/%Y-%H:%M:%S')
        self.view.play_first_round(start_date)
        match_list = self.mix_player(roster_list)
        for match in match_list:
            self.play_match(match)
        end_first_round = "🎌 Fin du Round 1 🎌"
        self.view.message(end_first_round)

    def mix_player(self, roster_list):
        """ Mélange les joueurs, et définit les matchs (joueur vs joueur) sous forme de liste"""
        random.shuffle(roster_list)
        size = 2
        sub_list = [roster_list[x: x + size] for x in range(0, len(roster_list), size)]
        return sub_list



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
            self.score_update_if_win(match_list[0])
        if result == 2:
            second_player_score = 1
            self.score_update_if_win(match_list[1])
        if result == 3:
            first_player_score = 0.5
            second_player_score = 0.5
            self.score_update_if_equality(match_list)
        match_result = (
            [first_player, first_player_score],
            [second_player, second_player_score],
        )
        return match_result

    def color_draw(self, first_player, second_player):
        """ Assignation des couleurs aléatoirement """
        color = ["Blanc ⚪", "Noir ⚫"]
        random.shuffle(color)
        self.view.color_draw(first_player, second_player, color)

    def score_update_if_win(self, player):
        """ Mets à jour le score du joueur gagnant """
        player["total_score"] = player["total_score"] + 1
        name = player["first_name"]
        last_name = player["last_name"]
        score = player["total_score"]
        equality = False
        self.view.display_new_score_if_win(name, last_name)

    def score_update_if_equality(self, match_list):
        """ Mets à jour les scores des joueurs ayant fait match nul """
        for player in match_list:
            player["total_score"] = player["total_score"] + 0.5
        self.view.display_new_score_if_equality()


















