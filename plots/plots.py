import numpy as np
import pandas as pd
import math as m
import matplotlib.pyplot as plt
import matplotlib

import sys
sys.path.append('../')
from calculations import coefficients as co
from classes import trial, simulation, experiment, model

def read_csv(path):
    return pd.read_csv(path, header =1, sep='\s*[;]\s*', index_col=False)

def quantile_quantile_plots(Dane,ModelA,ModelB,ModelC):
    
    
    
    fig = plt.figure(figsize=(10,10))
    ax1 = fig.add_subplot(221)
    plt.ylim(0, 1500)
    plt.xlim(0,1500)
    ax2 = fig.add_subplot(222)
    plt.ylim(0, 1500)
    plt.xlim(0,1500)
    ax3 = fig.add_subplot(223)
    plt.ylim(0, 1500)
    plt.xlim(0,1500)
    
    
    ax1.plot(Dane.measurement,ModelA.sim_values,'ro',markersize = 2)    
    a1= np.arange(-1000,1500)
    b1=a1
    ax1.plot(a1,b1,color='black')
    ax1.set_xlabel('Model-A Conc. (pptv)')
    ax1.set_ylabel('Observed Conc. (pptv)')
    
    ax2.plot(Dane.measurement,ModelB.sim_values,'ro',markersize = 2,color='blue')
    ax2.plot(a1,b1,color='black')
    ax2.set_xlabel('Model-B Conc. (pptv)')
    ax2.set_ylabel('Observed Conc. (pptv)')
   
    ax3.plot(Dane.measurement,ModelC.sim_values,'ro',markersize = 2,color='green')
    ax3.plot(a1,b1,color='black')
    ax3.set_xlabel('Model-C Conc. (pptv)')
    ax3.set_ylabel('Observed Conc. (pptv)')
    
    plt.savefig('results/quantile_quantile_plot.png')
    
    plt.show()





#paths,sensory,modele,TH
def FractionalBiasFBdiagram(Data,ModelA,ModelB,ModelC,TH): 
   
    
    lim=3*len(Data.sensors)
    FBfp=[[0 for i in range(len(Data.sensors))] for j in range(3)]
    FBfn=[[0 for i in range(len(Data.sensors))] for j in range(3)]
    n=['0' for i in range(lim)]
    
    x=0
    y=0
    indexN=0
    modelA=True
    modelB=False
    modelC=False
    
    for i in range(lim):
        if(modelA):
            FBfp[x][y]=co.FBFP(ModelA.sim_sensors[y],Data.sensors[y],0)
            FBfn[x][y]=co.FBFN(ModelA.sim_sensors[y],Data.sensors[y],0)
            y+=1
            n[indexN]='ModelA'
            indexN+=1
            if(y==len(Data.sensors)):
                y=0
                x+=1
                modelA=False
                modelB=True
                continue
        if(modelB):
            FBfp[x][y]=co.FBFP(ModelB.sim_sensors[y],Data.sensors[y],0)
            FBfn[x][y]=co.FBFN(ModelB.sim_sensors[y],Data.sensors[y],0)
            y+=1
            n[indexN]='ModelB'
            indexN+=1
            if(y==len(Data.sensors)):
                y=0
                x+=1
                
                modelB=False
                modelC=True
                continue
        if(modelC):
            FBfp[x][y]=co.FBFP(ModelC.sim_sensors[y],Data.sensors[y],0)
            FBfn[x][y]=co.FBFN(ModelC.sim_sensors[y],Data.sensors[y],0)
            y+=1
            n[indexN]='ModelC'
            indexN+=1
            if(y==len(Data.sensors)):
                y=0
                x+=1
                modelC=False                
                continue
   
    
    
          
            
    
        
    A=np.array(FBfp)  
    B=np.array(FBfn)
    N=np.array(n)           #nazwy punktów
    
    plt.figure(figsize=(10,10))
    
    xy=[0,0.66,1.33,0.66,0]
    yy=[0.66,1.33,0.66,0,0]
    
    ax=plt.subplot(111)
    ax.fill(xy,yy,'y')
    a= np.arange(3)
    a2=np.arange(0,1,1/3)
    b=-a+2
    a1=np.arange(0,1.35,0.02)
    b1=a2+2/3    
    b2=a1-2/3
    a3=np.arange(0,1.1,0.1)
    b3=a3
    
    colours=['red','blue','yellow','green','purple','orange']
    
    for i in range(len(Data.sensors)):
        plt.plot(A[:,i],B[:,i],'ro',color=colours[i], label='ASP0'+str(i+1))
    
    #plt.plot(A[:,1],B[:,1],'bs',color='blue',label='ASP02')
    
    plt.plot(a2,b1,'m-.',a1,b2,'m-.',a3,b3,'m-.',a,b,color='black')
    
    k=0
    for i in range(3):
        for j in range(len(Data.sensors)):
            plt.annotate(N[k], (A[i,j],B[i,j]))
            k+=1
    
    
    ax.spines['right'].set_visible(False)
    ax.spines['top'].set_visible(False)
    plt.ylim(0, 2)
    plt.xlim(0,2)
    plt.legend()
    ax.set_xlabel('FBfn')
    ax.set_ylabel('FBfp')
    
    plt.savefig('results/FractionalBiasFBdiagram.png')
   
    plt.show()
    
    return 1 
    
def MGandVG(Data,ModelA,ModelB,ModelC,TH): 
   
    
    lim=3*len(Data.sensors)
    oVG=[[0 for i in range(len(Data.sensors))] for j in range(3)]
    oMG=[[0 for i in range(len(Data.sensors))] for j in range(3)]
    n=['0' for i in range(lim)]
    
    x=0
    y=0
    indexN=0
    modelA=True
    modelB=False
    modelC=False
    
    for i in range(lim):
        if(modelA):
            oVG[x][y]=co.VG(ModelA.sim_sensors[y],Data.sensors[y],0)
            oMG[x][y]=co.MG(ModelA.sim_sensors[y],Data.sensors[y],0)
            y+=1
            n[indexN]='ModelA'
            indexN+=1
            if(y==len(Data.sensors)):
                y=0
                x+=1
                modelA=False
                modelB=True
                continue
        if(modelB):
            oVG[x][y]=co.VG(ModelB.sim_sensors[y],Data.sensors[y],0)
            oMG[x][y]=co.MG(ModelB.sim_sensors[y],Data.sensors[y],0)
            y+=1
            n[indexN]='ModelB'
            indexN+=1
            if(y==len(Data.sensors)):
                y=0
                x+=1
                
                modelB=False
                modelC=True
                continue
        if(modelC):
            oVG[x][y]=co.VG(ModelC.sim_sensors[y],Data.sensors[y],0)
            oMG[x][y]=co.MG(ModelC.sim_sensors[y],Data.sensors[y],0)
            y+=1
            n[indexN]='ModelC'
            indexN+=1
            if(y==len(Data.sensors)):
                y=0
                x+=1
                modelC=False                
                continue   
        
    A=np.array(oMG)  
    B=np.array(oVG)
    
    N=np.array(n)           #nazwy punktów
    #ax=plt.subplot(111)
    plt.figure(figsize=(10,10))
    
    colours=['red','blue','yellow','green','purple','orange']
    
    for i in range(len(Data.sensors)):
        plt.loglog(A[:,i],B[:,i],'ro',color=colours[i], label='ASP0'+str(i+1))
        
    
    # plt.loglog(A[:,0],B[:,0],'ro',color='red',label='ASP01',basex=2,basey=2)
    # if (sensory==2):
    #     plt.plot(A[:,1],B[:,1],'bs',color='blue',label='ASP02')
    
    k=0
    for i in range(3):
        for j in range(len(Data.sensors)):
            plt.annotate(N[k], (A[i,j],B[i,j]))
            k+=1
    
    plt.axvline(x=0.5,linestyle='--',color='black')
    plt.axvline(x=2,color='black',linestyle='--')
    plt.axvline(x=1,color='black')
    plt.ylim(1, 16)
    plt.xlim(0.25,4)
    plt.legend()
    plt.xlabel('MG')
    plt.ylabel('VG')
    
    plt.savefig('results/MGandVG.png')
    
    plt.show()
    
    return 1



def MinMax(tab):
    wmin=2**30
    imin=0
    wmax=-273
    imax=0
    for i in range(len(tab)):
        if(tab[i]<wmin):
            wmin=tab[i]
            imin=i
        if(tab[i]>wmax):
            wmax=tab[i]
            imax=i
    return imin,imax

def sortuj_wstaw(tab,tab1,tab2):                                 
    n=len(tab)    
    for x in range(1, n):
        selected = tab[x]
        selected1=tab1[x]
        selected2=tab2[x]
                              
        y = x-1                                         
        while y >= 0 and selected2 < tab2[y]:             
            tab[y+1]=tab[y]
            tab1[y+1]=tab1[y]
            tab2[y+1] = tab2[y]                          
            y -= 1                                     
        
        tab[y+1] = selected
        tab1[y+1]=selected1
        tab2[y+1]=selected2
                                     
    return tab,tab1,tab2

def BoxPlot(Model,Data,Wind,n):
    lim = len(Model.sim_values)
    data=[0 for i in range(lim)]
    model=[0 for i in range(lim)]
    wind=[0 for i in range(lim)]
    windy=z = [[None for j in range(n)] for i in range(40)] 
    x=[0 for i in range(n)]
    for i in range(lim):
        data[i]=Data.measurement[i]
        model[i]=Model.sim_values[i]    
        wind[i]=Wind.Wind_speed[i]
    wmin=wind[MinMax(wind)[0]]
    wmax=wind[MinMax(wind)[1]]
    step=round((wmax-wmin)/(n-1),3)
    x[0]=wmin
    for i in range(1,n):
        x[i]=round(x[i-1]+step,3)
    
    data=sortuj_wstaw(data, model, wind)[0]
    model=sortuj_wstaw(data, model, wind)[1]
    wind=sortuj_wstaw(data, model, wind)[2]
    
    j=0
    k=0
    for i in range(lim):
        if(wind[i]<=x[j]):
            windy[k][j]=model[i]/data[i]
            k+=1
        else:
            j+=1
            k=0
    
    ax=plt.subplot()
    
    df = pd.DataFrame(windy,columns=x)
    

    
    boxplot = df.boxplot(column=x)
    boxplot.set_xlabel('m/s')
    boxplot.set_ylabel('Cp/Co')
    boxplot.set_yscale('log')

    plt.xlim(0,6)
    plt.ylim(0.1, 10)
    
    plt.plot([0,10],[1,1],color='black')
    plt.plot([0,10],[2,2],color='black',linestyle='--')
    plt.plot([0,10],[0.5,0.5],color='black',linestyle='--')
    
    plt.savefig('results/BoxPlot.png')
    
    plt.show()
    
    return 1


        


#Data= pd.read_csv('ASP01.txt', header =1, sep='\s*[;]\s*', index_col=False,engine='python' )             #Dane rzeczywiste 
#Model = pd.read_csv('ASP01_MODEL-C.txt', header =1, sep='\s*[;]\s*',index_col=False,engine='python' )   #Dane modelowe
#Wind=pd.read_csv('MS01.txt', header =1, sep='\s*[;]\s*', index_col=False,engine='python' )

#print(Data)             sep='\s*[;]\s*'
#print(Data.iat[0,3])
#print(Model.dtypes)
#print(Model.iloc[0:7,0:7])
paths=['ASP01.txt','ASP01_MODEL-A.txt','ASP01_MODEL-B.txt','ASP01_MODEL-C.txt','ASP02.txt','ASP02_MODEL-A.txt','ASP02_MODEL-B.txt','ASP02_MODEL-C.txt'] 

#print(Wind.iloc[:,4])


#FractionalBiasFBdiagram(paths, 2, 3,0)
#quantilpaths=['ASP01.txt','ASP01_MODEL-A.txt','ASP01_MODEL-B.txt','ASP01_MODEL-C.txt']
#quantile_quantile_plots(quantilpaths)
#MGandVG(paths, 2, 3,0)
#BoxPlot(Model, Data, Wind,5)



# exp1= experiment.Experiment(r'C:\Users\Kamil Prasuła\Desktop\Praktyki\DANE\BTEX_NOWY\BTEX\BTEX.txt')

# sensor_exp=exp1.trials[0].sensors[0]
# print(sensor_exp.measurement)       #Data
# print('-----------')
# modelA= model.Model('model1a', exp1)

# modelA.sims[0].add_sensor(R'C:\Users\Kamil Prasuła\Desktop\Praktyki\DANE\BTEX_NOWY\MODEL-A\ASP01_MODEL-A.txt')
# sensorA=modelA.sims[0].sim_sensors[0]
# print(sensorA.sim_values)           #Model
# print('-----------------')
# meteo1=exp1.trials[0].meteo_stations[0]
# wspeed1=meteo1.Wind_speed           #Wind
# print(wspeed1)


                     

exp = experiment.Experiment(r'C:\Users\Kamil\Desktop\BTEX_NOWY\BTEX\BTEX.txt')

sensors=exp.trials[0]
#print(len(sensors.sensors))
sensor1=exp.trials[0].sensors[0]        #Data
meteo1=exp.trials[0].meteo_stations[0]  #Wind 


modelA = model.Model('Model-A', exp)
modelA.sims[0].add_sensor(R'C:\Users\Kamil\Desktop\BTEX_NOWY\MODEL-A\ASP01_MODEL-A.txt')
modelA.sims[0].add_sensor(R'C:\Users\Kamil\Desktop\BTEX_NOWY\MODEL-A\ASP02_MODEL-A.txt')

sensorA=modelA.sims[0]
sensor1A=modelA.sims[0].sim_sensors[0]
sensor2A=modelA.sims[0].sim_sensors[1]


 


modelB = model.Model('Model-B', exp)
modelB.sims[0].add_sensor(R'C:\Users\Kamil\Desktop\BTEX_NOWY\MODEL-B\ASP01_MODEL-B.txt')
modelB.sims[0].add_sensor(R'C:\Users\Kamil\Desktop\BTEX_NOWY\MODEL-B\ASP02_MODEL-B.txt')

sensorB=modelB.sims[0]
sensor1B=modelB.sims[0].sim_sensors[0]
sensor2B=modelB.sims[0].sim_sensors[1]



modelC = model.Model('Model-C', exp)
modelC.sims[0].add_sensor(R'C:\Users\Kamil\Desktop\BTEX_NOWY\MODEL-C\ASP01_MODEL-C.txt')
modelC.sims[0].add_sensor(R'C:\Users\Kamil\Desktop\BTEX_NOWY\MODEL-C\ASP02_MODEL-C.txt')

sensorC=modelC.sims[0]
sensor1C=modelC.sims[0].sim_sensors[0]
sensor2C=modelC.sims[0].sim_sensors[1]


#quantile_quantile_plots(sensor1,sensor1A,sensor1B,sensor1C)
#BoxPlot(sensor1C, sensor1, meteo1,5)
#FractionalBiasFBdiagram(sensors,sensorA,sensorB,sensorC, 0)
MGandVG(sensors,sensorA,sensorB,sensorC, 0)