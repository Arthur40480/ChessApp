""" Les joueurs """

class Joueur:
    """ Modèle de joueur """

    def __init__(self, nom, prenom, date_de_naissance):
        """ Initialise les valeurs d'un joueur via le constructeur __init__ """

        self.nom = nom
        self.prenom = prenom
        self.date_de_naissance = date_de_naissance

