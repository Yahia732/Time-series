import numpy as np


class outliers:
    def __init__(self,percentage_outliers=0.05):
        """
        Parameters:

            percentage_outliers (float): The percentage of outliers to add (e.g., 0.2 for 20%).

        """
        self.percentage_outliers=percentage_outliers

    def add_outliers(self,data):
        """
        Add outliers to the time series data.

        Parameters:
            data (numpy.ndarray): The time series data.

        Returns:
            numpy.ndarray: The time series data with outliers.
        """
        # data = pd.Series(data)
        num_outliers = int(len(data) * self.percentage_outliers)
        outlier_indices = np.random.choice(len(data), num_outliers, replace=False)
        # data_with_outliers = pd.Series(data.copy())
        data_with_outliers = data.copy()
        outliers = np.random.uniform(-1, 1, num_outliers)
        anomaly_mask = np.zeros(len(data_with_outliers), dtype=bool)
        if len(outliers) > 0:
            data_with_outliers[outlier_indices] = outliers
            anomaly_mask[outlier_indices] = True

        return data_with_outliers, anomaly_mask
