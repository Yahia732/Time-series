import numpy as np


class cycle:
    def __init__(self, cyclic_periods, season_type):
        """

        cyclic_periods (str): The type of cyclic periods ('No Cyclic Periods', 'Short Cycles', or 'Long Cycles').

        """
        self.cyclic_periods=cyclic_periods
        self.season_type=season_type

    def add_cycles(self,data):
        """
        Add cyclic component to the time series data.

        Parameters:
            data (DatetimeIndex): The time index for the data.


        Returns:
            numpy.ndarray: The cyclic component of the time series.
        """
        if self.cyclic_periods == "exist":  # Quarterly
            cycle_component = 1 if self.season_type == 'multiplicative' else 0
            cycle_component += np.sin(2 * np.pi * (data.quarter - 1) / 4)
        else:  # No Cyclic Periods
            cycle_component = 0 if self.season_type == 'additive' else 1

        return cycle_component