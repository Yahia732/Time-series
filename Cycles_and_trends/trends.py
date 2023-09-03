import random

import numpy as np
import pandas as pd
from datetime import datetime, timedelta


class trends:
    def __init__(self, trend, data_size, data_type):
        """
    Parameters:
        trend (str): The magnitude of the trend ('No Trend', 'Small Trend', 'Large Trend').
        """
        self.trend=trend
        self.data_size=data_size
        self.data_type=data_type

    def add_trend(self,data):
        """
        Add trend component to the time series data.

        Parameters:
            data (DatetimeIndex): The time index for the data.


        Returns:
            numpy.ndarray: The trend component of the time series.
        """
        if self.trend == "exist":
            slope = random.choice([1, -1])
            trend_component = np.linspace(0, self.data_size / 30 * slope, len(data)) if slope == 1 else np.linspace(
                -1 * self.data_size / 30, 0, len(data))
        else:  # No Trend
            trend_component = np.zeros(len(data)) if self.data_type == 'additive' else np.ones(len(data))

        return pd.Series(trend_component)