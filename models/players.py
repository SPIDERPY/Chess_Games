

class Players:
    """Joueurs."""
    
    def __init__(self, last_name, first_name, date_of_birth, sex, ranking):
        """Initialise un joueur avec:
        - son nom
        - son prénom
        - sa date d'anniversaire
        - son sexe
        - son classement
        """
        self.last_name = last_name
        self.first_name = first_name
        self.date_of_birth = date_of_birth
        self.sex = sex
        self.ranking = ranking
        