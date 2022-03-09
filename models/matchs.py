

class Match:
    """Création d'un match."""
    def __init__(self, player1, player2, score1, score2):
        """Initialise un match avec un joueur1, joueur2
        et le score
        """

        
        self.result = ([player1, score1], [player2, score2])