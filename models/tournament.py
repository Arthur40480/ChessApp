""" Les tournois """

class Tournament:
    """ Modèle de tournoi """

    def __init__(
        self,
        name,
        place,
        start_date,
        end_date,
        description,
        players_list,
        round_list,
        current_score,
        nbr_rounds=4,
        current_round=1,
        finished=False
   ):
        """ Initialise les valeurs d'un tournoi via le constructeur __init__ """

        self.name = name
        self.place = place
        self.start_date = start_date
        self.end_date = end_date
        self.nbr_rounds = nbr_rounds
        self.current_round = current_round
        self.round_list = round_list
        self.players_list = players_list
        self.description = description
        self.finished = finished
        self.current_score = current_score
