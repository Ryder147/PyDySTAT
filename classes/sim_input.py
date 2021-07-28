# -*- coding: utf-8 -*-

class Sim_Input:
    
    def __init__(self, trial):
        self.__setup_sim_input(trial)
        
    def __setup_sim_input(self, trial):
        self.sim_sources = trial.sources.copy()
        self.sim_meteo_stations = trial.meteo_stations.copy()
        self.sim_sensors = trial.sensors.copy()
