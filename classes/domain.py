# -*- coding: utf-8 -*-

class Domain:
    
    def __init__(self, S, W, N, E, min_H, max_H):
        self.set_bounds(S, W, N, E, min_H, max_H)
        
    def set_bounds(self, S, W, N, E, min_H, max_H):
        self.SOUTH_BOUND = S
        self.WEST_BOUND = W
        self.NORTH_BOUND = N
        self.EAST_BOUND = E
        self.Min_height = min_H
        self.Max_height = max_H