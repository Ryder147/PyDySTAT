# -*- coding: utf-8 -*-

class Substance:
    
    def __init__(self, name, unit, CAS_Number, molar_mass, density):
        self.__set_substance(name, unit, CAS_Number, molar_mass, density)
        
    def __set_substance(self, name, unit, CAS_Number, molar_mass, density):
        self.name = name
        self.unit = unit
        self.CAS_Number = CAS_Number
        self.molar_mass = molar_mass
        self.density = density