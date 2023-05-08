# -*- coding: utf-8 -*-

import pandas as pd
import sys
sys.path.append('../')
from classes import location, time_sequence

class Sensor:

    def __init__(self, sensor_series, path):
        self.__setup_sensor(sensor_series)
        self.__setup_measurements(path)
        
    def __setup_sensor(self, sensor):
        self.name = sensor[0]
        self.loc = location.Location(sensor[2],
                            sensor[1],
                            sensor[3].split()[0])
        
    def __setup_measurements(self, path):
        self.measurement = []
        self.time_seq = []
        df = pd.read_csv(
            path, 
            skiprows = 1,
            header = 0,
            sep = "\s*[;]\s*",
            engine = 'python',
            index_col=False)
        
        for i in range(0, df.shape[0]):
            self.measurement.append(df.iloc[i][3])
            self.time_seq.append(time_sequence.Time_Sequence(
                df.iloc[i][0], 
                df.iloc[i][1], 
                df.iloc[i][2]))