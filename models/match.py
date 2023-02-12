""" Les matchs """

class Match:
    """ Modèle de match """

    def __init__(self, joueur1, joueur2, score1, score2):
        """ Initialise les valeurs d'un match via le constructeur __init__ """

        self.joueur1 = joueur1
        self.joueur2 = joueur2
        self.score1 = score1
        self.score2 = score2