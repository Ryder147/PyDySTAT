# -*- coding: utf-8 -*-

import pandas as pd
import os.path
import sensor, source

class Simulation:
    
    def __init__(self, path):
        self.sim_sensors = []
        self.sim_sources = []
        self.__setup_sim(path)
        
    def __setup_sim(self, path):
        file = open(path)
        sources_start_line = 0
        sensors_start_line = 0
        i = 1
    
        line = file.readline()
        for line in file:
            if(line == '/* SOURCE DESCRIPTION:\n'):
                sources_start_line = i+1
            elif(line == '/* MEASUREMENT DESCRIPTION:\n'):
                sensors_start_line = i+1
            i+=1
                
        self.__add_sources(self.__read_dataframe(path, sources_start_line, sensors_start_line - sources_start_line - 3), path)
        self.__add_sensors(self.__read_dataframe(path, sensors_start_line), path)
        
    def __read_dataframe(self, path, description_start, description_len = None):
        return pd.read_csv(
            path, 
            nrows = description_len,
            skiprows = description_start, 
            header = 0, 
            sep = "\s*[;]\s*",
            engine = 'python')
    
    def __add_sensors(self, sensors_df, path):
        for i in range(0, sensors_df.shape[0]):
            self.sim_sensors.append(sensor.Sensor(
                sensors_df.iloc[i], 
                os.path.dirname(path) + '\\' + sensors_df.iloc[i][0] + '.txt'))
        
    def __add_sources(self, sources_df, path):
        for i in range(0, sources_df.shape[0]):
            self.sim_sources.append(source.Source(
                sources_df.iloc[i],
                os.path.dirname(path) + '\\' + sources_df.iloc[i][0] + '.txt'))
        
    #def get_Sim_Sensor_Output(self):
        