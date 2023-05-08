# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt

def draw_map(experiment, trial):
    # TODO
    #   do zautomatyzowania sciaganie mapy eksperymentu
    #   na podstawie experiment.domain
    map_im = plt.imread(r'C:\Users\orgin\Desktop\studia\praktyki\DANE_1\BTEX\map.png')
    
    exp_domain = experiment.domain
    BBox = np.array([exp_domain.WEST_BOUND, exp_domain.EAST_BOUND,      
         exp_domain.SOUTH_BOUND, exp_domain.NORTH_BOUND], dtype = float)
    fig, ax = plt.subplots(figsize = (8,7))
    
    
    ax.scatter([trial.sensors[i].loc.x for i in range(0, len(trial.sensors))],
               [trial.sensors[i].loc.y for i in range(0, len(trial.sensors))],
               zorder=1, alpha= 1, c='b', s=10)
    ax.scatter([trial.sources[i].loc.x for i in range(0, len(trial.sources))],
               [trial.sources[i].loc.y for i in range(0, len(trial.sources))],
               alpha= 1, c='r', s=100, marker=(5, 2))
    
    ax.set_title(experiment.experiment_name)
    ax.set_xlim(BBox[0],BBox[1])
    ax.set_ylim(BBox[2],BBox[3])
    ax.imshow(map_im, zorder=0, extent = BBox, aspect= 'equal')
    
    plt.savefig('results/map.png')