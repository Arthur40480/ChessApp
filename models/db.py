from tinydb import TinyDB, Query

""" La base de donnée """

class Database:

    def __init__(self):
        self.db = TinyDB("data/players_db.json")
        self.players_table = self.db.table("Players")
        self.db_tournament = TinyDB("data/tournaments_db.json")
        self.tournament_table = self.db_tournament.table("Tournaments")
        self.user = Query()

    """ ----- ----- Joueur ----- ----- """
    def checks_players_already_exists(self, chess_id, first_name, last_name):
        """ On vérifie si le joueur n'éxiste pas déjà dans la base de donnée """
        same_chess_id = self.players_table.search(self.user.chess_id == chess_id)
        same_name = self.players_table.search(self.user.first_name == first_name)
        same_last_name = self.players_table.search(self.user.last_name == last_name)
        if same_chess_id or same_name and same_last_name:
            return True

    def add_player_in_file(self, data):
        """ Enregistre le joueur dans la base de donnée """
        self.players_table.insert(data)

    def display_player_list(self):
        """ Retourne la liste des joueurs par ordre alphabétique """
        players = sorted(self.players_table, key=lambda player: player['last_name'])
        return players

    def player_list_by_score(self, player_list):
        """ Retourne la liste des joueurs par ordre de celui qui à le plus de points """
        sorted_match_list = sorted(player_list, key=lambda player: player[1], reverse=True)
        return sorted_match_list

    """ ----- ----- TOURNOI ----- ----- """
    def add_tournament_in_file(self, data):
        """ Enregistre le tournoi dans la base de donnée """
        self.tournament_table.insert(data)

    def end_tournament(self, tournament):
        """ Modifie la valeur de FINISHED """
        name = tournament["name"]
        self.tournament_table.upsert({"name": name, "finished": True}, self.user.name == name)

    def retrieve_current_tournament(self, name):
        """ On récupère le tournoi actuel dans la base de donnée"""
        current_tournament = self.tournament_table.get(self.user.name == name)
        return current_tournament

    def update_tournament_file(self,
                               list_player_current_score,
                               name,
                               round_list,
                               tournament,
                               nbr_rounds,
                               next_round
                               ):
        """ On enregistre les rounds et matchs du tournoi dans la base de données"""
        list_current_score = sorted(list_player_current_score, key=lambda player: player[1], reverse=True)
        self.tournament_table.upsert({"name": name, "current_score": list_current_score}, self.user.name == name)
        self.tournament_table.upsert({"name": name, "round_list": round_list}, self.user.name == name)
        if tournament["current_round"] == tournament["nbr_rounds"]:
            self.tournament_table.upsert({"name": name, "current_round": nbr_rounds}, self.user.name == name)
        else:
            self.tournament_table.upsert({"name": name, "current_round": next_round}, self.user.name == name)
