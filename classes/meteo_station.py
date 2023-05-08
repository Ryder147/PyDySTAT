# -*- coding: utf-8 -*-'

import sys
sys.path.append('../')
from classes import location, time_sequence as ts
import pandas as pd

class Meteo_Station:
    
    def __init__(self, station_series, path):
        self.name = station_series[0]
        self.loc = location.Location(station_series[2],
                                     station_series[1],
                                     station_series[3].split()[0])
        self.time_seq = []
        self.Temperature = []
        self.Wind_speed = []
        self.Wind_direction = []
        self.Mixing_height = []
        self.PG_stability_class = []
        
        self.__setup_meteo_station(path)
        
    def __setup_meteo_station(self, path):
        df = self.__read_dataframe(path)
        
        for i in range(0, df.shape[0]):
            row = df.iloc[i]
            self.time_seq.append(ts.Time_Sequence(row[0], row[1], row[2]))
            self.Temperature.append(row[3])
            self.Wind_speed.append(row[4])
            self.Wind_direction.append(row[5])
            self.Mixing_height.append(row[6])
            self.PG_stability_class.append(row[7])
    
    def __read_dataframe(self, path):
        return pd.read_csv(
            path, 
            skiprows = 1,
            header = 0,
            sep = "\s*[;]\s*",
            engine = 'python',
            index_col=False)