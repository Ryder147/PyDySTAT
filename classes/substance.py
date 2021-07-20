# -*- coding: utf-8 -*-

class Substance:
    
    def __init__(self, name, unit):
        self.__set_substance(name, unit)
        
    def __set_substance(self, name, unit):
        self.name = name
        self.unit = unit
        #self.CAS_Number # string
        #self.molar_mass # float
        #self.density    # float