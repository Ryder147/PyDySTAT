# -*- coding: utf-8 -*-

import pandas as pd
import source, sensor

class Trial:
    
    def __init__(self, path, sensors_paths):
        self.__setup_trial(path, sensors_paths)
        
    def __setup_trial(self, path, sensors_paths):
        self.sensors = []
        self.sources = []
        self.__parse_trial(path, sensors_paths)
        
    def __parse_trial(self, path, sensors_paths):
        file = open(path)
        sources_start_line = 0
        sensors_start_line = 0
        i = 1
        trial_des = {}
    
        line = file.readline()
        for line in file:
            if(line == '/* SOURCE DESCRIPTION:\n'):
                sources_start_line = i+1
            elif(line == '/* MEASUREMENT DESCRIPTION:\n'):
                sensors_start_line = i+1
                
            if(sources_start_line == 0 and sensors_start_line == 0):
                line = line.replace('\n', "")
                line = line.replace('\t', "")
        
                splitted_line = line.split(':', 1)
        
                if(len(splitted_line) == 2):
                    trial_des[splitted_line[0]] = splitted_line[1].strip()
            i+=1
                
        self.trial_name = trial_des['TRIAL NAME']
        self.__add_sources(self.__read_dataframe(path, sources_start_line, sensors_start_line - sources_start_line - 3))
        self.__add_sensors(self.__read_dataframe(path, sensors_start_line), sensors_paths)
        
    def __add_sensors(self, sensors_df, sensors_paths):
        for i in range(0, sensors_df.shape[0]):
            self.sensors.append(sensor.Sensor(sensors_df.iloc[i][:], sensors_paths[i]))
        
    def __add_sources(self, sources_df):
        for i in range(0, sources_df.shape[0]):
            self.sources.append(source.Source(sources_df.iloc[i][:]))
        
    def __read_dataframe(self, path, description_start, description_len = None):
        return pd.read_csv(
            path, 
            nrows = description_len,
            skiprows = description_start, 
            header = 0, 
            sep = "\s*[;]\s*",
            engine = 'python')