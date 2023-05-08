# -*- coding: utf-8 -*-

import sys, os.path
sys.path.append('../')
from classes import domain, substance, trial

class Experiment:
    
    def __init__(self, path):
        exp_des = self.__parse_exp_input(path)
        self.experiment_name = exp_des['EXPERIMENT NAME']
        self.sub = substance.Substance(
            exp_des['TRACER'],
            exp_des['UNIT'],
            exp_des['CAS_NUMBER'],
            exp_des['MOLAR_MASS'],
            exp_des['DENSITY'])
        self.__set_domain(exp_des)
        self.__add_trials(self.__parse_trials_paths(path))
        
    def __add_trials(self, trials_paths):
        self.trials = []
        for i in range(0, len(trials_paths)):
            self.trials.append(trial.Trial(trials_paths[i]))
        
    def __parse_trials_paths(self, path):
        file = open(path)
        
        line = file.readline()
        while(line != '/* TRIALS LIST:\n'):
            line = file.readline()
            
        path = os.path.dirname(path)
        trials_paths = []
        line = file.readline()
        
        while(len(line) != 0):
            trials_paths.append(path + '\\' + line.rstrip() + '.txt')
            line = file.readline()
            
        return trials_paths
        
    def __parse_exp_input(self, path):
        file = open(path)
        exp_des = {}
    
        for line in file:
            line = line.replace('\n', "")
            line = line.replace('\t', "")
        
            splitted_line = line.split(':', 1)
        
            if(len(splitted_line) == 2):
                try:
                    exp_des[splitted_line[0]] = float(splitted_line[1])
                except:
                    exp_des[splitted_line[0]] = splitted_line[1].strip()
            
        
        exp_des['MINIMUM ELEVATION'] = float(exp_des['MINIMUM ELEVATION'].split()[0])
        exp_des['MAXIMUM ELEVATION'] = float(exp_des['MAXIMUM ELEVATION'].split()[0])
        
        return exp_des
        
    def __set_domain(self, exp_des):
        self.domain = domain.Domain(
            exp_des['SOUTH-BOUND LATITUDE'],
            exp_des['WEST-BOUND LONGITUDE'],
            exp_des['NORTH-BOUND LATITUDE'],
            exp_des['EAST-BOUND LONGITUDE'],
            exp_des['MINIMUM ELEVATION'],
            exp_des['MAXIMUM ELEVATION'])