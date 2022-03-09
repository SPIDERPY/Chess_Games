

class Round:
    """Tournées."""
    
    def __init__(self, name, start_date_and_time, en_date_and_time):
        self.name = name
        self.start_date = start_date_and_time
        self.end_date = en_date_and_time
        