import numpy as np
import pandas as pd

from Seasonality.seasonality import seasonality


class Daily_Seasonality(seasonality):
    def add_daily_seasonality(self,data):
        """
        Add seasonality component to the time series data.

        Parameters:
            data (DatetimeIndex): The time index for the data.


        Returns:
            numpy.ndarray: The seasonal component of the time series.
        """
        if self.seasonality == "exist":  # Daily Seasonality
            seasonal_component = np.sin(2 * np.pi * data.hour / 24)
            seasonal_component += 1 if self.season_type == 'multiplicative' else 0
        else:
            seasonal_component = np.zeros(len(data)) if self.season_type == 'additive' else np.ones(len(data))
        return pd.Series(seasonal_component)
