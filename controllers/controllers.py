from views.views import View
from models.player import Player
from models.tournament import Tournament
from models.db import Database
from models.tour import Tour
from datetime import datetime
from datetime import date
import random
import os


class Controller:

    """ ----- ----- Menu ----- ----- """
    def __init__(self):
        """Initialise les valeurs du Controller via le constructeur"""
        self.view = View()
        self.database = Database()

    def display_menu(self):
        """ Fait apparaître le menu """
        welcom_title = "♟️ Chess App ♟️"
        self.add_folder_data()
        self.view.message(welcom_title)
        user_choice = self.view.menu()
        if user_choice == 1:
            self.new_player()
        if user_choice == 2:
            self.new_tournament()
        if user_choice == 3:
            self.display_tournament_not_finished()
        if user_choice == 4:
            self.display_rapport_menu_title()
        if user_choice == 5:
            exit()

    def add_folder_data(self):
        if not os.path.exists("data"):
            os.mkdir("data")

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
            self.display_round_and_match()
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
        chess_id = data_player[2]
        b_day = data_player[3]
        b_month = data_player[4]
        b_year = data_player[5]
        try:
            b_day = int(b_day)
            b_month = int(b_month)
            b_year = int(b_year)
        except ValueError:
            print("")
            print("🚨 La date de naissance indiqué est incorrect ! 🚨")
            self.display_menu()
        else:
            dath_of_birth = date(b_year, b_month, b_day).strftime("%d/%m/%y")

        """ On viens vérifier si le joueur existe déjà """
        db_query = self.database.checks_players_already_exists(chess_id, first_name, last_name)
        if db_query is True:
            error_message = "⚠️ Ce joueur est déjà enregistrer ⚠️"
            self.view.message(error_message)
            self.display_menu()

        player = Player(last_name, first_name, dath_of_birth, chess_id)
        self.database.add_player_in_file(player.__dict__)
        self.view.add_player_in_file_title()
        new_player_again = input("🔄 Voulez vous enregistrer un autre joueur ? 🔄 (Oui/Non) :")
        if (new_player_again == "O" or new_player_again == "Oui" or new_player_again == "oui"):
            self.new_player()
        else:
            self.display_menu()

    def players_roster(self):
        """ Création d'une liste contenant les joueurs enregistrés """
        players = self.database.display_player_list()
        player_roster = []
        for people in players:
            player = Player(
                people["last_name"],
                people["first_name"],
                people["dath_of_birth"],
                people["chess_id"],
            ).__dict__
            player_roster.append(player)
        return player_roster

    def display_player_list(self):
        """ Affiche la liste des joueurs enregistrer par ordre alphabétique (Nom) """
        self.view.player_list_title()
        players = self.database.display_player_list()
        if len(players) == 0:
            error_message = "🚨 Aucun joueur enregistrer ! 🚨"
            self.view.message(error_message)
            self.display_menu_rapport()
        else:
            self.view.display_player_list(players)
            self.back_to_menu()

    def display_roster_list(self):
        """ Affiche les joueurs participant au tournoi séléctionner """
        tournament = self.tournament_list()
        self.view.display_tournament_list(tournament)
        if len(tournament) == 0:
            error_messsage = "🚨 Aucun tournoi enregistrer ! 🚨"
            self.view.message(error_messsage)
            self.display_menu_rapport()
        else:
            tournament_select = input("Veuillez ajouter le numéro du tournoi:")
            try:
                if int(tournament_select) > 0 and int(tournament_select) <= (len(tournament)):
                    tournament_select = int(tournament_select) - 1
                    self.view.display_roster_list(tournament[tournament_select])
                    self.back_to_menu()
                else:
                    print("")
                    print("🚨 Ce numéro de tournoi n'éxiste pas ! 🚨")
                    print("")
                    self.display_menu()
            except ValueError:
                error_message = "🔢️ Veuillez choisir un nombre 🔢️"
                self.view.message(error_message)
                self.display_menu()

    def display_victorious_player(self, ranking):
        """ On trie la liste des score finaux pour annoncer le vainqueur """
        ranking_list = sorted(ranking, key=lambda player: player[1], reverse=True)
        self.view.display_victorious_player(ranking_list)

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
        current_score = []
        finished = False
        tournament = Tournament(
            name,
            place,
            start_date,
            end_date,
            description,
            roster_list,
            round_list,
            current_score,
            round,
            current_round,
            finished,
        )
        self.database.add_tournament_in_file(tournament.__dict__)
        self.view.add_tournament_in_file_title()
        self.start_tournament(tournament.__dict__)

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
        tournament_list = self.database.tournament_table
        if len(tournament_list) == 0:
            error_messsage = "🚨 Aucun tournoi enregistrer ! 🚨"
            self.view.message(error_messsage)
            self.display_menu_rapport()
        else:
            self.view.display_tournament_list(tournament_list)
            self.back_to_menu()

    def display_tournament_not_finished(self):
        """ Affiche seulement les tournois en cours """
        self.view.tournament_not_finished_list_title()
        tournament_list = self.database.tournament_table
        tournament_list_not_finished = []
        for tournament in tournament_list:
            if tournament["finished"] is False:
                tournament_list_not_finished.append(tournament)
        if len(tournament_list_not_finished) == 0:
            error_messsage = "🚨 Aucun tournoi en cours ! 🚨"
            self.view.message(error_messsage)
            self.display_menu()
        else:
            self.view.display_tournament_not_finished(tournament_list_not_finished)
            tournament_select = input("Veuillez ajouter le numéro du tournoi à reprendre:")
            try:
                if int(tournament_select) > 0 and int(tournament_select) <= (len(tournament_list_not_finished)):
                    tournament_select = int(tournament_select) - 1
                    tournament = tournament_list_not_finished[tournament_select]
                    self.resume_tournament(tournament)
                else:
                    print("")
                    print("🚨 Ce numéro de tournoi n'éxiste pas ! 🚨")
                    print("")
                    self.display_menu()
            except ValueError:
                error_message = "🔢️ Veuillez choisir un nombre 🔢️"
                self.view.message(error_message)
                self.display_menu()

    def resume_tournament(self, tournament):
        """ Permet de reprendre un tournoi en cours suivant le round actuel """
        current_round = tournament["current_round"]
        if current_round == 1:
            self.play_first_round(tournament)
        else:
            current_score = tournament["current_score"]
            round_list = tournament["round_list"]
            match_list = []
            for round in round_list:
                matchs_list = round["match_list"]
                for match in matchs_list:
                    match_list.append(match)
            self.play_other_round(tournament, match_list, current_score)

    def tournament_list(self):
        """ Créer une liste de tous les tournois enregistrés """
        tournament_table = self.database.tournament_table
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
                tournament["current_score"],
                tournament["nbr_rounds"],
                tournament["current_round"],
                tournament["finished"],
            ).__dict__
            tournament_list.append(tournaments)
        return tournament_list

    def end_tournament(self, tournament):
        """ Annonce la fin du tournoi """
        self.database.end_tournament(tournament)
        end_tournament_title = " Fin du tournoi !"
        self.view.message(end_tournament_title)

    """ ----- ----- ROUND ----- ----- """
    def play_first_round(self, tournament):
        """ Annonce le premier Round """
        roster_list = tournament["players_list"]
        curent_round = tournament["current_round"]
        start_date = datetime.today().strftime('%d/%m/%Y-%H:%M:%S')
        self.view.play_round(curent_round, start_date)

        """ On définit les matchs """
        match_list = self.mix_player_first_round(roster_list)
        result_match_list = []

        """ On créer une liste qui vas contenir l'ensemble des matchs du tournoi """
        list_all_matchs = []
        for match in match_list:
            list_all_matchs.append(match)
            """ On viens chercher le résultat, et on l'ajoute à la liste de résultat """
            result_match_list.append(self.play_match_first_round(match))
        end_date = datetime.today().strftime('%d/%m/%Y-%H:%M:%S')

        """ Annonce de la fin du premier Round """
        end_first_round = f"🎌 Fin du Round 1 - {end_date} 🎌"
        self.view.message(end_first_round)

        """ On créer une liste qui vas contenir les scores actuels des joueurs """
        list_player_current_score = []
        for match_list in result_match_list:
            for match in match_list:
                list_player_current_score.append(match)

        """ On viens mettre à jour le round actuel, on enregistre le round dans la liste de round du tournoi """
        self.update_tournament_file(1, start_date, end_date, result_match_list, tournament, list_player_current_score)

        """ On passe au round suivant """
        self.ask_next_round(tournament, list_all_matchs, list_player_current_score)

    def mix_player_first_round(self, roster_list):
        """ Mélange les joueurs, et définit les matchs (joueur vs joueur) sous forme de liste """
        random.shuffle(roster_list)
        size = 2
        sub_list = [roster_list[x: x + size] for x in range(0, len(roster_list), size)]
        return sub_list

    def play_other_round(self, tournament, list_all_matchs, list_player_current_score):
        """ Annonce les autres Round """
        start_date = datetime.today().strftime('%d/%m/%Y-%H:%M:%S')
        current_round = tournament["current_round"]
        self.view.play_round(current_round, start_date)

        """ On définit les matchs """
        match_list = self.mix_player(list_all_matchs, list_player_current_score)
        result_match_list = []
        for match in match_list:
            """ On rajoute les matchs dans notre liste de matchs """
            list_all_matchs.append([match[0], match[2]])
            result_match_list.append(self.play_match_other_rounds(match))
        end_date = datetime.today().strftime('%d/%m/%Y-%H:%M:%S')

        """ Annonce de la fin du Round """
        end_round = f"🎌 Fin du Round {current_round} - {end_date} 🎌"
        self.view.message(end_round)

        """ On créer une liste qui vas contenir les scores actuels des joueurs mis à jour """
        list_current_score = []
        for match_list in result_match_list:
            for match in match_list:
                list_current_score.append(match)

        """ On viens mettre à jour le round actuel, on enregistre le round dans la liste de round """
        self.update_tournament_file(current_round, start_date, end_date, result_match_list,
                                    tournament, list_current_score)

        """ Si on arrive au dernier round, alors le tournoi est finis """
        nbr_round = tournament["nbr_rounds"]
        if int(current_round) == int(nbr_round):
            self.end_tournament(tournament)
            self.display_victorious_player(list_current_score)
            self.back_to_menu()
        else:
            self.ask_next_round(tournament, list_all_matchs, list_current_score)

    def mix_player(self, list_all_matchs, list_player_current_score):
        """ Définit les matchs, et évite de retomber sur le même joueur """
        sorted_match_list = self.database.player_list_by_score(list_player_current_score)
        match_list = []
        while len(sorted_match_list) != 0:
            i = 1
            player1 = sorted_match_list[0][0]
            score_player1 = sorted_match_list[0][1]
            player2 = sorted_match_list[i][0]
            score_player2 = sorted_match_list[i][1]
            match_1 = [player1, player2]
            match_verify = [player2, player1]

            if match_1 not in list_all_matchs and match_verify not in list_all_matchs or len(sorted_match_list) == 2:
                match_list.append([player1, score_player1, player2, score_player2])
                del sorted_match_list[i]
                del sorted_match_list[0]

            else:
                print("Le match à déjà été jouer")
                i += 1
                player1 = sorted_match_list[0][0]
                score_player1 = sorted_match_list[0][1]
                player2 = sorted_match_list[i][0]
                score_player2 = sorted_match_list[i][1]
                match_1 = [player1, player2]
                match_verify = [player2, player1]
                for n in range(len(sorted_match_list)):
                    if match_1 not in list_all_matchs \
                            and match_verify not in list_all_matchs \
                            or len(sorted_match_list) == 2:
                        match_list.append([player1, score_player1, player2, score_player2])
                        del sorted_match_list[i]
                        del sorted_match_list[0]
                        break
                    else:
                        i += 1
        return match_list

    def ask_next_round(self, tournament, list_all_matchs, list_player_current_score):
        """ Demande si on lance le round suivant """
        name = tournament["name"]
        current_tournament = self.database.retrieve_current_tournament(name)
        next_round = current_tournament["current_round"]
        answer = self.view.ask_next_round_title(next_round)
        if (answer == "O" or answer == "Oui" or answer == "oui"):
            self.play_other_round(current_tournament, list_all_matchs, list_player_current_score)
        else:
            self.display_menu()

    def update_tournament_file(self, current_round,
                               start_date,
                               end_date,
                               match_list,
                               tournament,
                               list_player_current_score
                               ):
        """ Enregistre les nouvelles données dans le fichier JSON """
        name = tournament["name"]
        round_list = tournament["round_list"]
        nbr_rounds = tournament["nbr_rounds"]
        next_round = current_round + 1
        round = Tour(
            f"Round {current_round}",
            start_date,
            end_date,
            match_list
        )
        index_list = int(current_round) - 1
        round_list.insert(index_list, round.__dict__)
        self.database.update_tournament_file(list_player_current_score,
                                             name,
                                             round_list,
                                             tournament,
                                             nbr_rounds,
                                             next_round)

    def display_round_and_match(self):
        """ Affiche les rounds, ainsi que les matchs de chaque round du tournoi séléctionner """
        tournament = self.tournament_list()
        if len(tournament) == 0:
            error_messsage = "🚨 Aucun tournoi en cours ! 🚨"
            self.view.message(error_messsage)
            self.display_menu_rapport()
        else:
            self.view.display_tournament_list(tournament)
            tournament_select = input("Veuillez ajouter le numéro du tournoi:")
            try:
                if int(tournament_select) > 0 and int(tournament_select) <= (len(tournament)):
                    tournament_select = int(tournament_select) - 1
                    self.view.display_round_and_match(tournament[tournament_select])
                    self.back_to_menu()
                else:
                    print("")
                    print("🚨 Ce numéro de tournoi n'éxiste pas ! 🚨")
                    print("")
                    self.display_menu()
            except ValueError:
                error_message = "🔢️ Veuillez choisir un nombre 🔢️"
                self.view.message(error_message)
                self.display_menu()

    """ ----- ----- MATCHS ----- ----- """
    def play_match_first_round(self, match_list):
        """ Lance les matchs du premier round """
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
        if result == 0 or result > 3:
            error_title = "⚠️ ERREUR: Ce résultat est incorrect ⚠️"
            self.view.message(error_title)
            self.display_menu()
        match_result = (
            [match_list[0], first_player_score],
            [match_list[1], second_player_score],
        )
        return match_result

    def play_match_other_rounds(self, match_list):
        """ Lance les matchs des rounds restants """
        first_player = match_list[0]["last_name"] + " " + match_list[0]["first_name"]
        second_player = match_list[2]["last_name"] + " " + match_list[2]["first_name"]
        first_player_score = match_list[1]
        second_player_score = match_list[3]
        self.view.match_title(first_player, second_player)
        self.color_draw(first_player, second_player)
        self.view.end_match()
        result = self.view.match_result(first_player, second_player)
        if result == 1:
            first_player_score = first_player_score + 1
        if result == 2:
            second_player_score = second_player_score + 1
        if result == 3:
            first_player_score = first_player_score + 0.5
            second_player_score = second_player_score + 0.5
        if result == 0 or result > 3:
            error_title = "⚠️ ERREUR: Ce résultat est incorrect ⚠️"
            self.view.message(error_title)
            self.display_menu()
        match_result = (
            [match_list[0], first_player_score],
            [match_list[2], second_player_score],
        )
        return match_result

    def color_draw(self, first_player, second_player):
        """ Assignation des couleurs aléatoirement """
        color = ["Blanc ⚪", "Noir ⚫"]
        random.shuffle(color)
        self.view.color_draw(first_player, second_player, color)
