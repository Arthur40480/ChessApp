from views.views import View
from models.player import Player
from tinydb import TinyDB, Query, where

class Controller:

    """ ----- ----- JOUEUR ----- ----- """
    def __init__(self):
        """ Initialise les valeurs du Conbtroller via le constructeur __init__ """
        self.db = TinyDB("db.json")
        self.players_table = self.db.table("Players")
        self.tournament_table = self.db.table("Tournament")
        self.view = View()
        self.user = Query()

    def display_title(self):
        """ Fait appraître le titre """
        welcom_title = "Bienvenue dans l'application de tournois d'echecs ♟️"
        self.view.message(welcom_title)
        self.display_menu()

    def display_menu(self):
        """ Fait appraître le menu """
        user_choice = self.view.menu()
        if user_choice == 1:
            self.new_player()
        if user_choice == 2:
            self.player_list()
        if user_choice == 3:
            self.upgrade_rank()

    def new_player(self):
        """ Créer un nouveau Joueur """
        player_creation_title = "Création d'un nouveau joueur 🙋"
        self.view.message(player_creation_title)
        data_player = self.view.new_player()
        first_name = data_player[0]
        last_name = data_player[1]
        dath_of_birth = data_player[2]
        rank = data_player[3]

        """ On viens vérifier si le joueur n'existe pas déjà """
        same_name = self.players_table.search(self.user.first_name == first_name)
        same_last_name = self.players_table.search(self.user.last_name == last_name)
        if same_last_name and same_name:
            error_message = "Ce joueur est déjà enregistrer ⚠️"
            self.view.message(error_message)
            self.display_menu()
        player = Player(last_name, first_name, dath_of_birth, rank)
        self.add_player(player.__dict__)

    def add_player(self, datas):
        """ Enregistre le joueur dans le fichier JSON """
        self.players_table.insert(datas)
        print(self.players_table.all())
        print("Joueur bien enregistrer 🎉")

    def player_list(self):
        """ Affiche la liste des joueurs enregistrer par ordre alphabétique (Nom) """
        list_title = "Liste des joueurs enregistrés 📃"
        self.view.message(list_title)
        players = self.players_table
        alphabetical_order_list = sorted(players, key=lambda player: player['last_name'])
        self.view.display_player_list(alphabetical_order_list)

    def upgrade_rank(self):
        """ Modifie le classement d'un joueur """
        rank_title = " Modification de classement 🏆"
        self.view.message(rank_title)
        datas_to_modify = self.view.modify_rank()
        last_name = datas_to_modify[0]
        first_name = datas_to_modify[1]
        rank = int(datas_to_modify[2])
        player_to_modify = self.players_table.search(self.user.last_name == last_name and self.user.first_name == first_name)
        print(type(player_to_modify))










