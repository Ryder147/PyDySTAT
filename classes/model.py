# -*- coding: utf-8 -*-

import re
import simulation, domain

class Model:
    
    #path -> path to model file
    #sim_paths -> list that contains paths to simulation files
    def __init__(self, path, sim_paths):
        self.sims = []
        
        model_des = self.__parse_model_input(path)
        self.model_name = model_des['MODEL NAME']
        self.__set_domain(model_des)
        
        for sim_path in sim_paths:
            self.__add_sim(sim_path)
        
    def __add_sim(self, sim_path):
        self.sims.append(simulation.Simulation(sim_path))
        
    def __parse_model_input(self, path):
        file = open(path)
        model_des = {}
    
        for line in file:
            line = line.replace('\n', "")
            line = line.replace('\t', "")
            line = re.sub('\s+', ' ', line)
        
            splitted_line = line.split(':', 1)
        
            if(len(splitted_line) == 2):
                try:
                    model_des[splitted_line[0]] = float(splitted_line[1])
                except:
                    model_des[splitted_line[0]] = splitted_line[1].strip()
            
        
        model_des['MODEL MINIMUM ELEVATION'] = float(model_des['MODEL MINIMUM ELEVATION'].split()[0])
        model_des['MODEL MAXIMUM ELEVATION'] = float(model_des['MODEL MAXIMUM ELEVATION'].split()[0])
        
        return model_des
        
    def __set_domain(self, model_des):
        self.model_domain = domain.Domain(
            model_des['MODEL SOUTH-BOUND LATITUDE'],
            model_des['MODEL WEST-BOUND LONGITUDE'],
            model_des['MODEL NORTH-BOUND LATITUDE'],
            model_des['MODEL EAST-BOUND LONGITUDE'],
            model_des['MODEL MINIMUM ELEVATION'],
            model_des['MODEL MAXIMUM ELEVATION'])
        
        
        
