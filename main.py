import random
import pandas as pd
import numpy as np
from datetime import datetime, timedelta
from sklearn.preprocessing import MinMaxScaler
from Seasonality.daily_seasonality import Daily_Seasonality
from Seasonality.weekly_seasonality import Weekly_Seasonality

from Cycles_and_trends.cycle import cycle
from Cycles_and_trends.trends import trends
from File_Manager.json_file import json_file
from File_Manager.yaml_file import yaml_file
from File_Manager.Configuration_Manager import configuration_manager
from Generator.Time_Series import Time_Series
from Noise.missing_values import missing_values
from Noise.noise import noise
from Noise.outliers import outliers
from Save.csv_file import csv_file

random.seed(22)





def main():
    Json_File = json_file("C:/Users/yahia.sedki/PycharmProjects/timeseriesgenerator/Time Series.json")
    # Yaml_File = yaml_file("C:/Users/yahia.sedki/PycharmProjects/timeseriesgenerator/Time Series.yaml")

    manager1 = configuration_manager(Json_File)
    variables_json = manager1.read()

    # manager2 = configuration_manager(Yaml_File)
    # start_date,end_date,variables_yaml = manager2.read()
    # Define simulation parameters
    Start_date = variables_json["Start Date"]
    End_date = variables_json["End Date"]
    frequencies = [variables_json["Sampling Frequency in Minutes"]]
    daily_seasonality_options = [variables_json["Daily Seasonality"]]
    weekly_seasonality_options = [variables_json["Weekly Seasonality"]]
    noise_levels = [variables_json["Noise Level"]]
    trend_levels = [variables_json["Trend Level"]]
    cyclic_periods = [variables_json["Cyclic Periods"]]
    data_types = [variables_json["Time-Series Data Type"]]
    percentage_outliers_options = [float(variables_json["Outliers Percentage"])]
    number_of_datasets = int(variables_json["Number of datasets to be generated"])
    start_date = datetime.strptime(Start_date, "%d/%m/%Y")
    end_date = datetime.strptime(End_date, "%d/%m/%Y")
    data_size = (end_date - start_date).days
    meta_data = []
    counter = 0
    # for freq in frequencies:
    for daily_seasonality in daily_seasonality_options:
        for weekly_seasonality in weekly_seasonality_options:
            for noise_level in noise_levels:
                for trend in trend_levels:
                    for cyclic_period in cyclic_periods:
                        for percentage_outliers in percentage_outliers_options:
                            for data_type in data_types:
                                for _ in  range(number_of_datasets):
                                    # for data_size in data_sizes:

                                    freq = random.choice(frequencies)
                                    counter += 1
                                    file_name = f"TimeSeries_daily_{daily_seasonality}_weekly_{weekly_seasonality}_noise_{noise_level}_trend_{trend}_cycle_{cyclic_period}_outliers_{int(percentage_outliers * 100)}%_freq_{freq}Days.csv"
                                    print(f"File '{file_name}' generated.")
                                    # Generate time index

                                    series= Time_Series(start_date, end_date, freq)
                                    date_rng=series.create_time_series()
                                    # Create components
                                    Daily_seasonality = Daily_Seasonality(daily_seasonality,
                                                                          season_type=data_type)
                                    daily_seasonal_component = Daily_seasonality.add_daily_seasonality(date_rng)
                                    Weekly_seasonality = Weekly_Seasonality(weekly_seasonality,
                                                                           season_type=data_type)
                                    weekly_seasonal_component = Weekly_seasonality.add_weekly_seasonality(date_rng)
                                    trnd = trends(trend, data_size=data_size,
                                                  data_type=data_type)
                                    trend_component = trnd.add_trend(date_rng)
                                    cyclic_period = "exist"
                                    Cycle=cycle(cyclic_period, season_type=data_type)
                                    cyclic_component = Cycle.add_cycles(date_rng)

                                    # Combine components and add missing values and outliers
                                    if data_type == 'multiplicative':
                                        data = daily_seasonal_component * weekly_seasonal_component * trend_component * cyclic_component
                                    else:
                                        data = daily_seasonal_component + weekly_seasonal_component + trend_component + cyclic_component
                                    # Create a MinMaxScaler instance
                                    scaler = MinMaxScaler(feature_range=(-1, 1))
                                    data = scaler.fit_transform(data.values.reshape(-1, 1))
                                    Noise=noise(noise_level)
                                    data = Noise.add_noise(data)
                                    Outliers=outliers(percentage_outliers)
                                    data, anomaly = Outliers.add_outliers(data)
                                    Missing_Value=missing_values(0.05)
                                    data = Missing_Value.add_missing_values(data)

                                    # Save the data to a CSV file
                                    df = pd.DataFrame({'value': data, 'timestamp': date_rng, 'anomaly': anomaly})
                                    file=csv_file('sample_datasets/' + str(counter) + '.csv',df)
                                    file.save()


                                    """
                                    import matplotlib.pyplot as plt
                                    plt.figure(figsize=(10, 6))
                                    # Plot the time series data
                                    plt.plot(df['timestamp'], df['value'], marker='o', linestyle='-', color='b',
                                             label='Time Series Data')
                                    # Add labels and title
                                    plt.xlabel('Time')
                                    plt.ylabel('Value')
                                    plt.title('Time Series Plot')
                                    plt.legend()
                                    # Display the plot
                                    plt.tight_layout()
                                    plt.show()
                                    break
                                    """

                                    meta_data.append({'id': str(counter) + '.csv',
                                                      'data_type': data_type,
                                                      'daily_seasonality': daily_seasonality,
                                                      'weekly_seasonality': weekly_seasonality,
                                                      'noise (high 30% - low 10%)': noise_level,
                                                      'trend': trend,
                                                      'cyclic_period (3 months)': cyclic_period,

                                                      'percentage_outliers': percentage_outliers,
                                                      'percentage_missing': 0.05,
                                                      'freq': freq})
                                    # generate_csv(list(zip(date_rng, data)), file_name)

    meta_data_df = pd.DataFrame.from_records(meta_data)
    meta_data_file = csv_file('sample_datasets/meta_data.csv', meta_data_df)
    meta_data_file.save()



if __name__ == "__main__":
    main()
