""" Les joueurs """
class Player:
    """ Modèle de joueur """
    def __init__(self, last_name, first_name, dath_of_birth, total_score=0):
        self.last_name = last_name
        self.first_name = first_name
        self.dath_of_birth = dath_of_birth
        self.total_score = total_score