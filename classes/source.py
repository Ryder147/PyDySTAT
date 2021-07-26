# -*- coding: utf-8 -*-

import pandas as pd
import location, time_sequence

class Source:
    
    def __init__(self, source_series, path):
        self.__setup_source(source_series, path)
        
    def __setup_source(self, source, path):
        self.name = source['SOURCE']
        self.loc = location.Location(source['LONGITUDE'],
                                     source['LATITUDE'],
                                     source['ELEVATION'].split()[0])
        self.device = source['METHOD/DEVICE']
        self.__parse_file(path)
    
    def __parse_file(self, path):
        df = pd.read_csv(
            path, 
            skiprows = 1,
            header = 0,
            sep = "\s*[;]\s*",
            engine = 'python',
            index_col=False)
        
        self.release_rate = []
        self.time_seq = []
        
        for i in range(0, df.shape[0]):
            row = df.iloc[i]
            self.release_rate.append(row[3])
            self.time_seq.append(time_sequence.Time_Sequence(
                row[0], 
                row[1], 
                row[2]))

    