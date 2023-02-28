""" Les tours """

class Tour:
    """ Modèle de tour """

    def __init__(self, nom, date_heure_debut, date_heure_fin, match_list):
        """ Initialise les attributs d'instance via le constructeur __init__ """

        self.nom = nom
        self.date_heure_debut = date_heure_debut
        self.date_heure_fin = date_heure_fin
        self.match_list = match_list

