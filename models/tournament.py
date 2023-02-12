""" Les tournois """

class Tournoi:
    """ Modèle de tournoi """

    def __init__(
        self,
        nom,
        lieu,
        date_de_debut,
        date_de_fin,
        nbr_de_tours="4",
        numero_tour_actuel,
        liste_des_tours,
        liste_des_joueurs,
        description,
    ):
        """ Initialise les valeurs d'un tournoi via le constructeur __init__ """

        self.nom = nom
        self.lieu = lieu
        self.date_de_debut = date_de_debut
        self.date_de_fin = date_de_fin
        self.nbr_de_tour = nbr_de_tours
        self.numero_tour_actuel = numero_tour_actuel
        self.liste_des_tours = liste_des_tours
        self.liste_des_joueurs = liste_des_joueurs
        self.description = description
