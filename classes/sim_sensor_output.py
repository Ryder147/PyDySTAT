# -*- coding: utf-8 -*-

import pandas as pd

class Sim_Sensor_Output:
    
    def __init__(self, path):
        self.sim_values = []
        self.__setup_sim_values(path)
        
    def __setup_sim_values(self, path):
        df = self.__read_dataframe(path)
        
        for i in range(0, df.shape[0]):
            self.sim_values.append(df.iloc[i, 3])
        
    def __read_dataframe(self, path):
        return pd.read_csv(
            path, 
            skiprows = 1,
            header = 0,
            sep = "\s*[;]\s*",
            engine = 'python',
            index_col=False)