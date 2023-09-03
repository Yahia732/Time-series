import numpy as np
import pandas as pd


class noise:
    def __init__(self,noise_level):
        """
      Parameters:
            noise_level (str): The magnitude of noise ('No Noise', 'Small Noise', 'Intermediate Noise', 'Large Noise').
        """
        self.noise_level=noise_level

    def add_noise(self,data):
        """
        Add noise component to the time series data.

        Parameters:
            data (DatetimeIndex): The time index for the data.


        Returns:
            numpy.ndarray: The noise component of the time series.
        """
        if self.noise_level == "small":
            noise_level = 0.1
            # noise = np.random.normal(0, 0.05, len(data))
        elif self.noise_level == "large":
            noise_level = 0.3
            # noise = np.random.normal(0, 0.1, len(data))
        else:  # No Noise
            noise_level = 0

        noise = np.zeros_like(data)
        for i in range(len(data)):
            noise[i] = np.random.normal(0, abs(data[i]) * noise_level) if noise_level > 0 else 0
        return pd.Series((data + noise)[:, 0])