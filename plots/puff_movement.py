import pandas as pd
import matplotlib.pyplot as plt

def read_dataframe(path):
    return pd.read_csv(
        path, 
        skiprows = 1, 
        header = 0,
        sep = "\s*[;]\s*",
        engine = 'python',
        index_col=False)

def puff_movement(observation, modelA, modelB, modelC, part_of_max = 0.1, log = False):
    data_frame = puff_mov_dataframe(observation, modelA, modelB, modelC, part_of_max)
    draw_plots(observation, modelA, modelB, modelC, data_frame, log)
    return data_frame
    
def puff_mov_dataframe(obs, modelA, modelB, modelC, part_of_max):
    columns = ['TOA', 'TOM', 'TOD', 'MV', 'DTA', 'DTD', 'DTR', 'DUR']
    df = pd.DataFrame(columns = columns)
    
    df = add_row(df, obs, part_of_max)
    df = add_row(df, modelA, part_of_max)
    df = add_row(df, modelB, part_of_max)
    df = add_row(df, modelC, part_of_max)
    df.index = ['Observation', 'Model A', 'Model B', 'Model C']
    
    return df

def add_row(df, values, part_of_max):
    row_dict = {}
    pptv_max_index = values[values.columns[3]].idxmax()
    
    row_dict['TOM'] = pptv_max_index    #values.iloc[pptv_max_index][0]
    row_dict['MV'] = values.iloc[pptv_max_index][3]
    row_dict['TOA'] = calculate_toa(values, part_of_max * row_dict['MV'], pptv_max_index)
    row_dict['TOD'] = calculate_tom(values, part_of_max * row_dict['MV'], pptv_max_index)
    row_dict['DTA'] = row_dict['TOM'] - row_dict['TOA']
    row_dict['DTD'] = row_dict['TOD'] - row_dict['TOM']
    row_dict['DTR'] = row_dict['DTA'] / row_dict['DTD']
    row_dict['DUR'] = row_dict['DTA'] + row_dict['DTD']
    
    return df.append(row_dict, ignore_index = True)
    
def calculate_toa(values, part_of_mv, pptv_max_index):
    for i in range(0, pptv_max_index):
        if(values.iloc[i][3] >= part_of_mv):
            return i    #values.iloc[i][0]
        
def calculate_tom(values, part_of_mv, pptv_max_index):
    for i in range(pptv_max_index, len(values.index)):
        if(values.iloc[i][3] <= part_of_mv):
            return i    #values.iloc[i][0]
        
def draw_plots(obs, modelA, modelB, modelC, puff_mov_df, log):
    plt.figure(figsize = (9,7))
    ax1 = plt.subplot2grid((10, 10), (0, 0), colspan=10, rowspan=9)
    ax2 = plt.subplot2grid((10, 10), (9, 0), colspan=10)
    colors = [['red', 'darkred'],
              ['magenta', 'orchid'],
              ['limegreen', 'green'],
              ['blue', 'darkblue']]

    if(log):
        ax1.semilogy(obs.index, obs[obs.columns[3]], c = colors[0][0])
        ax1.semilogy(modelA.index, modelA[modelA.columns[3]], c = colors[1][0])
        ax1.semilogy(modelB.index, modelB[modelB.columns[3]], c = colors[2][0])
        ax1.semilogy(modelC.index, modelC[modelC.columns[3]], c = colors[3][0])
    else:
        ax1.plot(obs.index, obs[obs.columns[3]], c = colors[0][0])
        ax1.plot(modelA.index, modelA[modelA.columns[3]], c = colors[1][0])
        ax1.plot(modelB.index, modelB[modelB.columns[3]], c = colors[2][0])
        ax1.plot(modelC.index, modelC[modelC.columns[3]], c = colors[3][0])

    ax2.set_xlim(ax1.get_xlim())
    ax1.get_xaxis().set_visible(False)
    ax2.get_yaxis().set_visible(False)

    ax2.set_xlabel('Time after puff release [min]')
    ax1.set_ylabel('Gas concentration [pptv]')
    ax1.legend(puff_mov_df.index)
    
    draw_hbar_plots(ax2, puff_mov_df, colors)
    plt.show()
    
def draw_hbar_plots(ax, puff_mov_df, colors, max_h = 1.0):
    bar_h = max_h/4
    
    draw_hbar_plot(ax, puff_mov_df, 0, colors[0], max_h, bar_h)
    draw_hbar_plot(ax, puff_mov_df, 1, colors[1], max_h, bar_h)
    draw_hbar_plot(ax, puff_mov_df, 2, colors[2], max_h, bar_h)
    draw_hbar_plot(ax, puff_mov_df, 3, colors[3], max_h, bar_h)
    
def draw_hbar_plot(ax, puff_mov_df, i, colors, max_h, bar_h):
    x1 = [puff_mov_df.iloc[i]['TOA'], 
         puff_mov_df.iloc[i]['TOA'], 
         puff_mov_df.iloc[i]['TOM'], 
         puff_mov_df.iloc[i]['TOM']]
    y = [max_h - i*bar_h,
         max_h - (i+1)*bar_h,
         max_h - (i+1)*bar_h,
         max_h - i*bar_h]
    x2 = [puff_mov_df.iloc[i]['TOM'], 
         puff_mov_df.iloc[i]['TOM'], 
         puff_mov_df.iloc[i]['TOD'], 
         puff_mov_df.iloc[i]['TOD']]
    
    ax.fill(x1, y, colors[0], x2, y, colors[1])

obs = read_dataframe(r'C:\Users\orgin\Desktop\studia\praktyki\DANE\BTEX\ASP02.txt')
modelA = read_dataframe(r'C:\Users\orgin\Desktop\studia\praktyki\DANE\BTEX\ASP02_MODEL-A.txt')
modelB = read_dataframe(r'C:\Users\orgin\Desktop\studia\praktyki\DANE\BTEX\ASP02_MODEL-B.txt')
modelC = read_dataframe(r'C:\Users\orgin\Desktop\studia\praktyki\DANE\BTEX\ASP02_MODEL-C.txt')

puff_mov_df = puff_movement(obs, modelA, modelB, modelC, log = True)
print(puff_mov_df)