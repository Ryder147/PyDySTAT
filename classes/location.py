# -*- coding: utf-8 -*-

class Location:
    
    def __init__(self, x, y, z):
        self.__set_location(x, y, z)
         
    def __set_location(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z