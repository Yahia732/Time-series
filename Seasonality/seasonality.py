from abc import ABC
class seasonality(ABC):
    def __init__(self,seasonality, season_type):
        """
        Parameters:
             seasonality (str): The type of seasonality ('Long', 'Short', or 'Intermediate').
        """
        self.seasonality=seasonality
        self.season_type=season_type


