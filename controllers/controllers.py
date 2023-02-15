from views.views import View
from models.player import Player
from tinydb import TinyDB, Query, where

class Controller:

    def __init__(self):
        """ Initialise les valeurs du Conbtroller via le constructeur __init__ """
        self.db = TinyDB("db.json")
        self.players_table = self.db.table("Players")
        self.tournament_table = self.db.table("Tournament")

    def displayTitle(self):
        """ Fait appraître le titre """
        welcom_title = "Bienvenue dans l'application de tournois d'echecs ♟️"
        title = View()
        title.welcome(welcom_title)
        self.displayMenu()

    def displayMenu(self):
        """ Fait appraître le menu """
        menu = View()
        user_choice = menu.menu()
        if user_choice == 1:
            self.newPlayer()

    def newPlayer(self):
        """ Créer un nouveau Joueur """
        player_creation_title = "Création d'un nouveau joueur 🙋"
        title = View()
        title.welcome(player_creation_title)
        data_player = title.newPlayer()
        first_name = data_player[0]
        last_name = data_player[1]
        dath_of_birth = data_player[2]
        rank = data_player[3]
        player = Player(first_name, last_name, dath_of_birth, rank)
        self.addPlayer(player.__dict__)

    def addPlayer(self, datas):
        """ Enregistre le joueur dans le fichier JSON """
        self.players_table.insert(datas)
        print(self.players_table.all())
        print("Joueur bien enregistrer 👍")


