# -*- coding: utf-8 -*-

import pandas as pd

def puff_mov_char(sensor_exp, sensor_output_A, sensor_output_B, sensor_output_C, part_of_max = 0.1):
    columns = ['TOA', 'TOM', 'TOD', 'MV', 'DTA', 'DTD', 'DTR', 'DUR']
    df = pd.DataFrame(columns = columns)
    
    df = __add_row(df, sensor_exp.measurement, part_of_max)
    df = __add_row(df, sensor_output_A.sim_values, part_of_max)
    df = __add_row(df, sensor_output_B.sim_values, part_of_max)
    df = __add_row(df, sensor_output_C.sim_values, part_of_max)
    df.index = ['Observation', 'Model A', 'Model B', 'Model C']
    
    return df

def __add_row(df, sensor_values, part_of_max):
    row_dict = {}
    pptv_max_index = __find_max_index(sensor_values)
    
    row_dict['TOM'] = pptv_max_index
    row_dict['MV'] = sensor_values[pptv_max_index]
    row_dict['TOA'] = __calculate_toa(sensor_values, part_of_max * row_dict['MV'], pptv_max_index)
    row_dict['TOD'] = __calculate_tom(sensor_values, part_of_max * row_dict['MV'], pptv_max_index)
    row_dict['DTA'] = row_dict['TOM'] - row_dict['TOA']
    row_dict['DTD'] = row_dict['TOD'] - row_dict['TOM']
    row_dict['DTR'] = row_dict['DTA'] / row_dict['DTD']
    row_dict['DUR'] = row_dict['DTA'] + row_dict['DTD']
    
    return df.append(row_dict, ignore_index = True)

def __find_max_index(v):
    i = 0
    max_i = i
    
    for x in v:
        if(x > v[max_i]):
            max_i = i
        i += 1
        
    return max_i
    
def __calculate_toa(sensor_values, part_of_mv, pptv_max_index):
    for i in range(0, pptv_max_index):
        if(sensor_values[i] >= part_of_mv):
            return i
        
def __calculate_tom(sensor_values, part_of_mv, pptv_max_index):
    for i in range(pptv_max_index, len(sensor_values)):
        if(sensor_values[i] <= part_of_mv):
            return i