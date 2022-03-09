

class Tournaments:
    """Tournois."""
    def __init__(self, name, location, date, number_of_turns=4, description):
        """Initialise un tournoi avec : 
        - son nom
        - son lieu
        - sa date
        - le nombre de tournées: par défault 4
        - la description
        """
        self.name = name
        self.location = location
        self.date = date
        self.number_of_turns = number_of_turns
        self.description = description
        self.joueurs = []
        self.rounds = []
    