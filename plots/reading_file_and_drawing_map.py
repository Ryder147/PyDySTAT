# -*- coding: utf-8 -*-
"""
Created on Tue Jul  6 11:00:04 2021

@author: orgin
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def read_experiment_description(path):
    file = open(path)
    exp_des = {}
    
    line = file.readline()
    while(line != "/* EXPERIMENT DESCRIPTION:\n"):
        line = file.readline()
    
    line = file.readline()
    while(not (line[0] == '/' and line[1] == '*')):
        line = line.replace('\n', "")
        line = line.replace('\t', "")
        
        splitted_line = line.split(':', 1)
        
        if(len(splitted_line) == 2):
            try:
                exp_des[splitted_line[0]] = float(splitted_line[1])
            except:
                exp_des[splitted_line[0]] = splitted_line[1]
                
        line = file.readline()
        
    return exp_des

def read_dataframes(path, description_start, description_length):
    return pd.read_csv(
        path, 
        skiprows = description_start, 
        nrows = description_length, 
        header = 0, 
        sep = "\s*[;]\s*",
        engine = 'python')

def draw_map(measurement_description, source_description, experiment_description, map_im):
    BBox = np.array([experiment_description['WEST-BOUND LONGITUDE'], experiment_description['EAST-BOUND LONGITUDE'],      
         experiment_description['SOUTH-BOUND LATITUDE'], experiment_description['NORTH-BOUND LATITUDE']], dtype = float)
    fig, ax = plt.subplots(figsize = (8,7))
    
    ax.scatter(measurement_description.LONGITUDE, measurement_description.LATITUDE, zorder=1, alpha= 1, c='b', s=10)
    ax.scatter(source_description.LONGITUDE, source_description.LATITUDE, alpha= 1, c='r', s=100, marker=(5, 2))
    
    ax.set_title(experiment_description['EXPERIMENT NAME'])
    ax.set_xlim(BBox[0],BBox[1])
    ax.set_ylim(BBox[2],BBox[3])
    ax.imshow(map_im, zorder=0, extent = BBox, aspect= 'equal')
    

path = r"C:\Users\orgin\Desktop\studia\praktyki\DANE_1\BTEX\BTEX_INPUT.txt"

experiment_description = read_experiment_description(path)
source_description = read_dataframes(path, 14, 1)
measurement_description = read_dataframes(path, 18, 14)

map_im = plt.imread(r'C:\Users\orgin\Desktop\studia\praktyki\DANE_1\BTEX\map.png')
draw_map(measurement_description, source_description, experiment_description, map_im)