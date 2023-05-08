# -*- coding: utf-8 -*-

# %%    0. importy

from classes import model, experiment
from calculations import coefficients as co
from calculations import puff_movement_characteristics as pmc
from plots import puff_movement as pm
from plots import drawing_map, plots

# %%    1. wczytanie experimentow i modeli (+ sensory modeli)

exp_btex_path = r'C:\Users\orgin\Desktop\studia\praktyki\BTEX_NOWY\BTEX\BTEX.txt'

modelA_sensor1_path = r'C:\Users\orgin\Desktop\studia\praktyki\BTEX_NOWY\MODEL-A\ASP01_MODEL-A.txt'
modelA_sensor2_path = r'C:\Users\orgin\Desktop\studia\praktyki\BTEX_NOWY\MODEL-A\ASP02_MODEL-A.txt'

modelB_sensor1_path = r'C:\Users\orgin\Desktop\studia\praktyki\BTEX_NOWY\MODEL-B\ASP01_MODEL-B.txt'
modelB_sensor2_path = r'C:\Users\orgin\Desktop\studia\praktyki\BTEX_NOWY\MODEL-B\ASP02_MODEL-B.txt'

modelC_sensor1_path = r'C:\Users\orgin\Desktop\studia\praktyki\BTEX_NOWY\MODEL-C\ASP01_MODEL-C.txt'
modelC_sensor2_path = r'C:\Users\orgin\Desktop\studia\praktyki\BTEX_NOWY\MODEL-C\ASP02_MODEL-C.txt'

exp = experiment.Experiment(exp_btex_path)
modelA = model.Model('Model-A', exp)
modelB = model.Model('Model-B', exp)
modelC = model.Model('Model-C', exp)

# dodanie sensorow z symulacji do kazdego modelu
modelA.sims[0].add_sensor(modelA_sensor1_path)
modelA.sims[0].add_sensor(modelA_sensor2_path)

modelB.sims[0].add_sensor(modelB_sensor1_path)
modelB.sims[0].add_sensor(modelB_sensor2_path)

modelC.sims[0].add_sensor(modelC_sensor1_path)
modelC.sims[0].add_sensor(modelC_sensor2_path)


# %%    2. miary -> calculations.cefficients.py

sensor_exp = exp.trials[0].sensors[0]
sensor_out_model = modelC.sims[0].sim_sensors[0]

print('Współczynnik             FB = ', co.FB(sensor_out_model, sensor_exp, 50))
print('Współczynnik           FBFN = ', co.FBFN(sensor_out_model, sensor_exp, 0))
print('Współczynnik           FBFP = ', co.FBFP(sensor_out_model, sensor_exp, 0))
print('Sprawdzenie    FB=FBFN-FBFP = ', co.FBFN(sensor_out_model, sensor_exp, 0)-co.FBFP(sensor_out_model, sensor_exp, 0))
print('Współczynnik             MG = ', co.MG(sensor_out_model, sensor_exp, 0))
print('Współczynnik           NMSE = ', co.NMSE(sensor_out_model, sensor_exp, 0))
print('Współczynnik              R = ', co.R(sensor_out_model, sensor_exp, 0))
print('Współczynnik             VG = ', co.VG(sensor_out_model, sensor_exp, 50))
print('Współczynnik           FACX = ', co.FACX(sensor_out_model, sensor_exp, 2,50))
print('Współczynnik            NSD = ', co.NSD(sensor_out_model, sensor_exp, 0))
print('Współczynnik          NRMSE = ',co.NRMSE(sensor_out_model, sensor_exp, 0))
print('Współczynnik            Afn = ',co.Afn(sensor_out_model, sensor_exp, 0))
print('Współczynnik            Afp = ',co.Afp(sensor_out_model, sensor_exp, 0))
print('Współczynnik            FMS = ',co.FMS(sensor_out_model, sensor_exp, 0))
print('Współczynnik          MOEfn = ',co.MOEfn(sensor_out_model, sensor_exp, 0))
print('Współczynnik          MOEfp = ',co.MOEfp(sensor_out_model, sensor_exp, 0))
print('Iloczyn               Ap Ao = ',co.iloczynApAo(sensor_out_model, sensor_exp, 0))


# %%    3. charakterystki ruchu chumry -> calculations.puff_movement_characteristics.py

sensor_exp = exp.trials[0].sensors[1]
sensor_output_A = modelA.sims[0].sim_sensors[1]
sensor_output_B = modelB.sims[0].sim_sensors[1]
sensor_output_C = modelC.sims[0].sim_sensors[1]

puff_mov_df = pmc.puff_mov_char(sensor_exp,
                                sensor_output_A,
                                sensor_output_B,
                                sensor_output_C,
                                part_of_max = 0.1) # domyslnie jest 0.1

print(puff_mov_df)

# %%    4. mapa eksperymentu (mapa, sensory, zrodla) -> plots.drawing_map.

trial = exp.trials[0]

drawing_map.draw_map(exp, trial)


# %%    5. wykres charakterystyk z punktu 3 -> plots.puff_movement.py

sensor_exp = exp.trials[0].sensors[1]
sensor_output_A = modelA.sims[0].sim_sensors[1]
sensor_output_B = modelB.sims[0].sim_sensors[1]
sensor_output_C = modelC.sims[0].sim_sensors[1]

# skala liniowa
# puff_mov_df rysuje plot oraz
# oblicza i zwraca DataFrame z charakterystykami ruchu chmury
puff_mov_df = pm.puff_movement(sensor_exp,
                               sensor_output_A,
                               sensor_output_B,
                               sensor_output_C,
                               part_of_max = 0.1, # domyslnie = 0.1
                               log = False)       # domyslnie = False

# skala logarytmiczna
# draw_plots rysuje ploty z charakterystykami
# ale nie oblicza ich, musimy podac je jako parametr
pm.draw_plots(sensor_exp,
              sensor_output_A,
              sensor_output_B,
              sensor_output_C,
              puff_mov_df, # DataFrame z wczesniej obliczonymi charakterystykami
              log = True)  # domyslnie False


# %%    6. plots.plots.py -> quantile_quantile_plots

sensor_exp = exp.trials[0].sensors[0]
sensor_output_A = modelA.sims[0].sim_sensors[0]
sensor_output_B = modelB.sims[0].sim_sensors[0]
sensor_output_C = modelC.sims[0].sim_sensors[0]

plots.quantile_quantile_plots(sensor_exp, sensor_output_A, sensor_output_B, sensor_output_C)

# %%    7. plots.plots.py -> BoxPlot

sensor_exp = exp.trials[0].sensors[0]
sensor_output_C = modelC.sims[0].sim_sensors[0]
meteo_station = exp.trials[0].meteo_stations[0]
parts_n = 5     # liczba pudełek na wykresie

plots.BoxPlot(sensor_output_C, sensor_exp, meteo_station, parts_n)

# %%    8. plots.plots.py -> FractionalBiasFBdiagram

trial = exp.trials[0]
sim_A = modelA.sims[0]
sim_B = modelB.sims[0]
sim_C = modelC.sims[0]
TH = 0

plots.FractionalBiasFBdiagram(trial, sim_A, sim_B, sim_C, TH)

# %%    9. plots.plots.py -> MGandVG

trial = exp.trials[0]
sim_A = modelA.sims[0]
sim_B = modelB.sims[0]
sim_C = modelC.sims[0]
TH = 0

plots.MGandVG(trial, sim_A, sim_B, sim_C, TH)
