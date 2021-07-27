# -*- coding: utf-8 -*-

import experiment, model

exp_path = r'C:\Users\orgin\Desktop\studia\praktyki\BTEX_NOWY\BTEX\BTEX.txt'
experiment = experiment.Experiment(exp_path)

modelA_path = r'C:\Users\orgin\Desktop\studia\praktyki\BTEX_NOWY\MODEL-A\MODEL-A.txt'
modelA_sim_paths = [r'C:\Users\orgin\Desktop\studia\praktyki\BTEX_NOWY\MODEL-A\MODEL-A_Sim1.txt']
modelA = model.Model(modelA_path, modelA_sim_paths)