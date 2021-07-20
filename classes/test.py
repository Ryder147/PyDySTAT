# -*- coding: utf-8 -*-

import experiment

exp_path = r'C:\Users\orgin\Desktop\studia\praktyki\DANE\BTEX\tmp\EXP.txt'
trials_paths = [r'C:\Users\orgin\Desktop\studia\praktyki\DANE\BTEX\tmp\TRIAL01.txt']
sensors_paths = [[r'C:\Users\orgin\Desktop\studia\praktyki\DANE\BTEX\tmp\ASP01.txt',
                r'C:\Users\orgin\Desktop\studia\praktyki\DANE\BTEX\tmp\ASP02.txt']]

experiment = experiment.Experiment(exp_path, trials_paths, sensors_paths)