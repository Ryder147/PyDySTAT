import pandas as pd
import matplotlib.pyplot as plt
import sys
sys.path.append('../')
from calculations import puff_movement_characteristics as pmc
from classes import experiment, model


def puff_movement(sensor_exp, sensor_output_A, sensor_output_B, sensor_output_C, part_of_max = 0.1, log = False):
    puff_mov_char_df = pmc.puff_mov_char(sensor_exp, sensor_output_A, sensor_output_B, sensor_output_C, part_of_max)
    draw_plots(sensor_exp, sensor_output_A, sensor_output_B, sensor_output_C, puff_mov_char_df, log)
    return puff_mov_char_df
        
def draw_plots(sensor_exp, sensor_output_A, sensor_output_B, sensor_output_C, puff_mov_df, log = False):
    plt.figure(figsize = (9,7))
    ax1 = plt.subplot2grid((10, 10), (0, 0), colspan=10, rowspan=9)
    ax2 = plt.subplot2grid((10, 10), (9, 0), colspan=10)
    colors = [['red', 'darkred'],
              ['magenta', 'orchid'],
              ['limegreen', 'green'],
              ['blue', 'darkblue']]

    if(log):
        ax1.semilogy(range(0, len(sensor_exp.measurement)), sensor_exp.measurement, c = colors[0][0])
        ax1.semilogy(range(0, len(sensor_output_A.sim_values)), sensor_output_A.sim_values, c = colors[1][0])
        ax1.semilogy(range(0, len(sensor_output_B.sim_values)), sensor_output_B.sim_values, c = colors[2][0])
        ax1.semilogy(range(0, len(sensor_output_C.sim_values)), sensor_output_C.sim_values, c = colors[3][0])
    else:
        ax1.plot(range(0, len(sensor_exp.measurement)), sensor_exp.measurement, c = colors[0][0])
        ax1.plot(range(0, len(sensor_output_A.sim_values)), sensor_output_A.sim_values, c = colors[1][0])
        ax1.plot(range(0, len(sensor_output_B.sim_values)), sensor_output_B.sim_values, c = colors[2][0])
        ax1.plot(range(0, len(sensor_output_C.sim_values)), sensor_output_C.sim_values, c = colors[3][0])

    ax2.set_xlim(ax1.get_xlim())
    ax1.get_xaxis().set_visible(False)
    ax2.get_yaxis().set_visible(False)

    ax2.set_xlabel('Time after puff release [min]')
    ax1.set_ylabel('Gas concentration [pptv]')
    ax1.legend(puff_mov_df.index)
    
    __draw_hbar_plots(ax2, puff_mov_df, colors)
    plt.show()
    
def __draw_hbar_plots(ax, puff_mov_df, colors, max_h = 1.0):
    bar_h = max_h/4
    
    __draw_hbar_plot(ax, puff_mov_df, 0, colors[0], max_h, bar_h)
    __draw_hbar_plot(ax, puff_mov_df, 1, colors[1], max_h, bar_h)
    __draw_hbar_plot(ax, puff_mov_df, 2, colors[2], max_h, bar_h)
    __draw_hbar_plot(ax, puff_mov_df, 3, colors[3], max_h, bar_h)
    
def __draw_hbar_plot(ax, puff_mov_df, i, colors, max_h, bar_h):
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

exp = experiment.Experiment(r'C:\Users\orgin\Desktop\studia\praktyki\BTEX_NOWY\BTEX\BTEX.txt')

modelA = model.Model('Model-A', exp)
modelA.sims[0].add_sensor(r'C:\Users\orgin\Desktop\studia\praktyki\BTEX_NOWY\MODEL-A\ASP01_MODEL-A.txt')
modelA.sims[0].add_sensor(r'C:\Users\orgin\Desktop\studia\praktyki\BTEX_NOWY\MODEL-A\ASP02_MODEL-A.txt')

modelB = model.Model('Model-B', exp)
modelB.sims[0].add_sensor(r'C:\Users\orgin\Desktop\studia\praktyki\BTEX_NOWY\MODEL-B\ASP01_MODEL-B.txt')
modelB.sims[0].add_sensor(r'C:\Users\orgin\Desktop\studia\praktyki\BTEX_NOWY\MODEL-B\ASP02_MODEL-B.txt')

modelC = model.Model('Model-C', exp)
modelC.sims[0].add_sensor(r'C:\Users\orgin\Desktop\studia\praktyki\BTEX_NOWY\MODEL-C\ASP01_MODEL-C.txt')
modelC.sims[0].add_sensor(r'C:\Users\orgin\Desktop\studia\praktyki\BTEX_NOWY\MODEL-C\ASP02_MODEL-C.txt')

puff_mov_df = puff_movement(exp.trials[0].sensors[1],
                            modelA.sims[0].sim_sensors[1],
                            modelB.sims[0].sim_sensors[1],
                            modelC.sims[0].sim_sensors[1],
                            log = True)
print(puff_mov_df)