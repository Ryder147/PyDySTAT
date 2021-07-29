# -*- coding: utf-8 -*-

import sys
sys.path.append('../')
from classes import simulation, domain

class Model:
    
    def __init__(self, name, experiment):
        self.model_name = name
        self.sims = []
        self.sub = experiment.sub
        
        self.__set_domain(experiment.domain)
        self.__add_sims(experiment)
        
    def __add_sims(self, experiment):
        for trial in experiment.trials:
            self.sims.append(simulation.Simulation(trial))
        
    def __set_domain(self, exp_domain):
        self.model_domain = domain.Domain(
            exp_domain.SOUTH_BOUND,
            exp_domain.WEST_BOUND,
            exp_domain.NORTH_BOUND,
            exp_domain.EAST_BOUND,
            exp_domain.Min_height,
            exp_domain.Max_height)
        