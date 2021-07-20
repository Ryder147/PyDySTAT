# -*- coding: utf-8 -*-

import domain, substance, trial

class Experiment:
    
    #trials_paths -> lista ze sciezkami do plikow trial
    #sensors_paths -> lista list sciezek do plikow z sensorami
    #sensors_paths[i][j] -> sciezka do sensora j dla triala i
    def __init__(self, path, trials_paths, sensors_paths):
        exp_des = self.__parse_exp_input(path)
        self.experiment_name = exp_des['EXPERIMENT NAME']
        self.sub = substance.Substance(exp_des['TRACER'], exp_des['UNIT'])
        self.__set_domain(exp_des)
        self.__add_trials(trials_paths, sensors_paths)
        
    def __add_trials(self, trials_paths, sensors_paths):
        self.trials = []
        for i in range(0, len(trials_paths)):
            self.trials.append(trial.Trial(trials_paths[i], sensors_paths[i]))
        
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