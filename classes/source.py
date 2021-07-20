# -*- coding: utf-8 -*-

import location

class Source:
    
    def __init__(self, source_series):
        self.__setup_source(source_series)
        
    def __setup_source(self, source):
        self.name = source['SOURCE']
        self.loc = location.Location(source['LONGITUDE'],
                                     source['LATITUDE'],
                                     source['ELEVATION'].split()[0])
        self.device = source['METHOD/DEVICE']