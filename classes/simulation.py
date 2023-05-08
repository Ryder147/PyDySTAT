# -*- coding: utf-8 -*-

import sys
sys.path.append('../')
from classes import sim_sensor_output, sim_input

class Simulation:
    
    def __init__(self, trial):
        self.sim_name = 'SIM-' + trial.trial_name
        self.sim_sensors = []
        self.sim_input = sim_input.Sim_Input(trial)
        
    def add_sensor(self, path):
        self.sim_sensors.append(sim_sensor_output.Sim_Sensor_Output(path))
        
    #def get_Sim_Sensor_Output(self):
        