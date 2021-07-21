# -*- coding: utf-8 -*-

import pandas as pd

def puff_mov_char(obs, modelA, modelB, modelC, part_of_max = 0.1):
    columns = ['TOA', 'TOM', 'TOD', 'MV', 'DTA', 'DTD', 'DTR', 'DUR']
    df = pd.DataFrame(columns = columns)
    
    df = __add_row(df, obs, part_of_max)
    df = __add_row(df, modelA, part_of_max)
    df = __add_row(df, modelB, part_of_max)
    df = __add_row(df, modelC, part_of_max)
    df.index = ['Observation', 'Model A', 'Model B', 'Model C']
    
    return df

def __add_row(df, values, part_of_max):
    row_dict = {}
    pptv_max_index = values[values.columns[3]].idxmax()
    
    row_dict['TOM'] = pptv_max_index    #values.iloc[pptv_max_index][0]
    row_dict['MV'] = values.iloc[pptv_max_index][3]
    row_dict['TOA'] = __calculate_toa(values, part_of_max * row_dict['MV'], pptv_max_index)
    row_dict['TOD'] = __calculate_tom(values, part_of_max * row_dict['MV'], pptv_max_index)
    row_dict['DTA'] = row_dict['TOM'] - row_dict['TOA']
    row_dict['DTD'] = row_dict['TOD'] - row_dict['TOM']
    row_dict['DTR'] = row_dict['DTA'] / row_dict['DTD']
    row_dict['DUR'] = row_dict['DTA'] + row_dict['DTD']
    
    return df.append(row_dict, ignore_index = True)
    
def __calculate_toa(values, part_of_mv, pptv_max_index):
    for i in range(0, pptv_max_index):
        if(values.iloc[i][3] >= part_of_mv):
            return i    #values.iloc[i][0]
        
def __calculate_tom(values, part_of_mv, pptv_max_index):
    for i in range(pptv_max_index, len(values.index)):
        if(values.iloc[i][3] <= part_of_mv):
            return i    #values.iloc[i][0]