
import numpy as np
import pandas as pd
import math as m
import matplotlib.pyplot as plt
import matplotlib

def read_csv(path):
    return pd.read_csv(path, header =1, sep='\s*[;]\s*', index_col=False)

def quantile_quantile_plots(paths):
    Dane=read_csv(paths[0])
    ModelA=read_csv(paths[1])
    ModelB=read_csv(paths[2])
    ModelC=read_csv(paths[3])
    
    
    fig = plt.figure(figsize=(10,10))
    ax1 = fig.add_subplot(221)
    ax2 = fig.add_subplot(222)
    ax3 = fig.add_subplot(223)
    
    
    ax1.plot(Dane[Dane.columns[3]],ModelA[ModelA.columns[3]],'ro',markersize = 2)    
    a1= np.arange(1500)
    b1=a1
    ax1.plot(a1,b1,color='black')
    ax1.set_xlabel('Model-A Conc. (pptv)')
    ax1.set_ylabel('Observed Conc. (pptv)')
    ax2.plot(Dane[Dane.columns[3]],ModelB[ModelB.columns[3]],'ro',markersize = 2,color='blue')
    ax2.plot(a1,b1,color='black')
    ax2.set_xlabel('Model-B Conc. (pptv)')
    ax2.set_ylabel('Observed Conc. (pptv)')
    ax3.plot(Dane[Dane.columns[3]],ModelC[ModelC.columns[3]],'ro',markersize = 2,color='green')
    ax3.plot(a1,b1,color='black')
    ax3.set_xlabel('Model-C Conc. (pptv)')
    ax3.set_ylabel('Observed Conc. (pptv)')
    plt.ylim(0, 1500)
    plt.xlim(0,1500)
    plt.show()

def FractionalBiasFBdiagram(paths,sensory,modele,TH): #(tablica cieżek, liczba sensorów,liczba modeli)
    model=1
    sensor=0
    lim=sensory*modele
    FBfp=[[0 for i in range(sensory)] for j in range(modele)]
    FBfn=[[0 for i in range(sensory)] for j in range(modele)]
    n=['0' for i in range(lim)]
    
   
    index=0
    x=0
    y=0
    for i in range(len(paths)):
        if(sensor>=len(paths) or model>=len(paths)):
            break
        FBfp[x][y]=FBFP(read_csv(paths[model]),read_csv(paths[sensor]),TH)
        FBfn[x][y]=FBFN(read_csv(paths[model]),read_csv(paths[sensor]),TH)
        x+=1
        n[index]=paths[model]
        index+=1
        model+=1
        if(model-1==modele):
            model+=1
            sensor=sensor+modele+1
            y+=1
            x=0    
        
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
    plt.plot(A[:,0],B[:,0],'ro',color='red',label='ASP01')
    plt.plot(A[:,1],B[:,1],'bs',color='blue',label='ASP02')
    #plt.plot(a,b,color='black')
    plt.plot(a2,b1,'m-.',a1,b2,'m-.',a3,b3,'m-.',a,b,color='black')
    
    k=0
    for i in range(sensory):
        for j in range(modele):
            plt.annotate(N[k], (A[j,i],B[j,i]))
            k+=1
    
    
    ax.spines['right'].set_visible(False)
    ax.spines['top'].set_visible(False)
    plt.ylim(0, 2)
    plt.xlim(0,2)
    plt.legend()
    ax.set_xlabel('FBfn')
    ax.set_ylabel('FBfp')
   
    plt.show()
    print(N)
    return 1 
    
def MGandVG(paths,sensory,modele,TH):
    model=1
    sensor=0
    lim=sensory*modele
    oVG=[[0 for i in range(sensory)] for j in range(modele)]
    oMG=[[0 for i in range(sensory)] for j in range(modele)]
    n=['0' for i in range(lim)]
    
   
    index=0
    x=0
    y=0
    for i in range(len(paths)):
        if(sensor>=len(paths) or model>=len(paths)):
            break
        oVG[x][y]=VG(read_csv(paths[model]),read_csv(paths[sensor]),TH)
        
        oMG[x][y]=MG(read_csv(paths[model]),read_csv(paths[sensor]),TH)
        x+=1
        n[index]=paths[model]
        index+=1
        model+=1
        if(model-1==modele):
            model+=1
            sensor=sensor+modele+1
            y+=1
            x=0    
        
    A=np.array(oMG)  
    B=np.array(oVG)
    print(A)
    print(B)
    N=np.array(n)           #nazwy punktów
    #ax=plt.subplot(111)
    plt.figure(figsize=(10,10))
    plt.loglog(A[:,0],B[:,0],'ro',color='red',label='ASP01',basex=2,basey=2)
    if (sensory==2):
        plt.plot(A[:,1],B[:,1],'bs',color='blue',label='ASP02')
    
    k=0
    for i in range(sensory):
        for j in range(modele):
            plt.annotate(N[k], (A[j,i],B[j,i]))
            k+=1
    #a1=np.arange(0.5,0.5,0)
    #a2=np.arange(2,2,0)
    #b=np.arange(1,17,1)
    #plt.plot(a1,b,a2,b,color='black')
    plt.axvline(x=0.5,linestyle='--',color='black')
    plt.axvline(x=2,color='black',linestyle='--')
    plt.axvline(x=1,color='black')
    plt.ylim(1, 16)
    plt.xlim(0.25,4)
    plt.legend()
    plt.xlabel('MG')
    plt.ylabel('VG')
    return 1
    
def VG(Model,Data,TH):          #geometric variance
    lim = len(Model['Modeled values'])
    suma=0
    
    data=0
    model=0
    ilosc=0
    
    lim1=Model.iloc[:,3].shape[0]
    lim2=Data.iloc[:,3].shape[0]
    if(lim1!=lim2):     #sprawdzenie czy Dane rzeczywiste i modelowe są tej samej długoci
        return -9
    
    for i in range(lim):
        data=Data.iat[i,3]
        model=Model.iat[i,3]
        if (data==-9 or model==-9):        #odrzucenie danych które są równe -9           
            continue
        if(data<TH):
            data=TH
        if(model<TH):
            model=TH
        suma+=(m.log(data)-m.log(model))**2
        ilosc+=1
        
    srednia=suma/ilosc
    VG=m.exp(srednia)
    return round(VG,2)
        
def FACX(Model,Data,x,TH):          #fraction of predictions X
    lim=len(Model['Modeled values'])
    licznik=0
    data=0
    model=0
    wynik=0
    
    lim1=Model.iloc[:,3].shape[0]
    lim2=Data.iloc[:,3].shape[0]
    if(lim1!=lim2):     #sprawdzenie czy Dane rzeczywiste i modelowe są tej samej długoci
        return -9
    
    for i in range(lim):
        data=Data.iat[i,3]
        model=Model.iat[i,3]
        
        if (data==-9 or model==-9):        #odrzucenie danych które są równe -9           
            continue
        if(data<TH):
            data=TH
        if(model<TH):
            model=TH
            
        if(1/x<(data/model)<x):
            licznik+=1
        wynik=licznik/lim
    return round(wynik,2)

def FB(Model,Data,TH):              #fractional bias
    lim=len(Model['Modeled values'])
    
    data=0
    model=0
    ilosc=0
    lim1=Model.iloc[:,3].shape[0]
    lim2=Data.iloc[:,3].shape[0]
    if(lim1!=lim2):     #sprawdzenie czy Dane rzeczywiste i modelowe są tej samej długoci
        return -9    
    
    sCo=float(0.0)          
    sCp=float(0.0)          
    for i in range(lim):
        data=Data.iat[i,3]
        model=Model.iat[i,3]
        
        if (data==-9 or model==-9):        #odrzucenie danych które są równe -9           
            continue
        if(data<TH):
            data=TH
        if(model<TH):
            model=TH
        
        sCo+=data
        sCp+=model
        ilosc+=1
    
    sCo=sCo/ilosc            #srednia Co
    sCp=sCp/ilosc             #srednia Cp 
    
    FB=2*(sCo-sCp)/(sCo+sCp)
    
    return round(FB, 3)
 
def FBFN(Model,Data,TH):            #fractional bias false negative
    
    lim=len(Model['Modeled values']) 
    suma1=0
    suma2=0
    
    data=0
    model=0
    ilosc=0
    lim1=Model.iloc[:,3].shape[0]
    lim2=Data.iloc[:,3].shape[0]
    if(lim1!=lim2):     #sprawdzenie czy Dane rzeczywiste i modelowe są tej samej długoci
        return -9 
    
    for i in range(lim):
        data=Data.iat[i,3]
        model=Model.iat[i,3]
        
        if (data==-9 or model==-9):        #odrzucenie danych które są równe -9           
            continue
        if(data<TH):
            data=TH
        if(model<TH):
            model=TH
            
        suma1+=(abs(data-model)+(data-model))
        suma2+=(data+model)
    FBFN=(0.5*suma1)/(0.5*suma2)
    return round(FBFN,3)

def FBFP(Model,Data,TH):            #fractional bias false positive
    lim=len(Model['Modeled values'])
    suma1=0
    suma2=0   
    
    data=0
    model=0
    ilosc=0
    lim1=Model.iloc[:,3].shape[0]
    lim2=Data.iloc[:,3].shape[0]
    if(lim1!=lim2):     #sprawdzenie czy Dane rzeczywiste i modelowe są tej samej długoci
        return -9 
    
    for i in range(lim):
        data=Data.iat[i,3]
        model=Model.iat[i,3]
        
        if (data==-9 or model==-9):        #odrzucenie danych które są równe -9           
            continue
        if(data<TH):
            data=TH
        if(model<TH):
            model=TH
            
        suma1+=(abs(data-model)+(model-data))
        suma2+=(data+model)
    FBFP=(0.5*suma1)/(0.5*suma2)
    return round(FBFP,3)
 
def MG(Model,Data,TH):          #geometric mean bias
    slnCo=0
    slnCp=0
    lim=len(Model['Modeled values'])
    
    data=0
    model=0
    ilosc=0
    lim1=Model.iloc[:,3].shape[0]
    lim2=Data.iloc[:,3].shape[0]
    if(lim1!=lim2):     #sprawdzenie czy Dane rzeczywiste i modelowe są tej samej długoci
        return -9 
    
    for i in range(lim):
        data=Data.iat[i,3]
        model=Model.iat[i,3]
        
        if (data==-9 or model==-9):        #odrzucenie danych które są równe -9           
            continue
        if(data<TH):
            data=TH
        if(model<TH):
            model=TH
            
        slnCo+=m.log(Data.iat[i,3])
        slnCp+=m.log(Model.iat[i,3])
        ilosc+=1
        
    slnCp=slnCp/ilosc
    slnCo=slnCo/ilosc
    
    MG=m.exp(slnCo-slnCp)
    return round(MG,2)

def NMSE(Model, Data,TH):           #normalized mean square error
    lim=len(Model['Modeled values'])
    sCo=float(0.0)          
    sCp=float(0.0)
    suma=0
         
    data=0
    model=0
    ilosc=0
    lim1=Model.iloc[:,3].shape[0]
    lim2=Data.iloc[:,3].shape[0]
    if(lim1!=lim2):     #sprawdzenie czy Dane rzeczywiste i modelowe są tej samej długoci
        return -9 
    
    for i in range(lim):
        data=Data.iat[i,3]
        model=Model.iat[i,3]
        
        if (data==-9 or model==-9):        #odrzucenie danych które są równe -9           
            continue
        if(data<TH):
            data=TH
        if(model<TH):
            model=TH
            
        sCo+=data
        sCp+=model
        suma+=(data-model)**2
        ilosc+=1
        
    sCo=sCo/ilosc             #srednia Co
    sCp=sCp/ilosc             #srednia Cp
    NMSE=(suma)/(ilosc*(sCo*sCp))
    return round(NMSE,2)

def R(Model,Data,TH):           #correlation coefficient
    lim=len(Model['Modeled values'])
    
    sCo=float(0.0)          
    sCp=float(0.0)  
        
    data=0
    model=0
    ilosc=0
    lim1=Model.iloc[:,3].shape[0]
    lim2=Data.iloc[:,3].shape[0]
    if(lim1!=lim2):     #sprawdzenie czy Dane rzeczywiste i modelowe są tej samej długoci
        return -9 
    
    for i in range(lim):
        data=Data.iat[i,3]
        model=Model.iat[i,3]
        
        if (data==-9 or model==-9):        #odrzucenie danych które są równe -9           
            continue
        if(data<TH):
            data=TH
        if(model<TH):
            model=TH
        
        sCo+=data
        sCp+=model
        ilosc+=1
    
    sCo=sCo/ilosc            #srednia Co
    sCp=sCp/ilosc            #srednia Cp 
    suma=0
    suma1=0
    suma2=0
    
    data=0
    model=0
    ilosc=0
    lim1=Model.iloc[:,3].shape[0]
    lim2=Data.iloc[:,3].shape[0]
    if(lim1!=lim2):     #sprawdzenie czy Dane rzeczywiste i modelowe są tej samej długoci
        return -9 
    
    for i in range(lim):
        data=Data.iat[i,3]
        model=Model.iat[i,3]
        
        if (data==-9 or model==-9):        #odrzucenie danych które są równe -9           
            continue
        if(data<TH):
            data=TH
        if(model<TH):
            model=TH
        
        suma+=(data-sCo)*(model-sCp)
        suma1+=(data-sCo)**2
        suma2+=(model-sCp)**2
        ilosc+=1
        
    roCo=m.sqrt(suma1/(ilosc))
    roCp=m.sqrt(suma2/(ilosc))
    
    R=(((1/ilosc)*suma)/(roCo*roCp))
    return round(R,3)

def NSD(Model, Data, TH):
    lim=len(Model['Modeled values'])
    qCp=0
    qCo=0
    sredniaCp=0
    sredniaCo=0
    sumaCp=0
    sumaCo=0    
    wynik=0
    
    data=0
    model=0
    ilosc=0
    lim1=Model.iloc[:,3].shape[0]
    lim2=Data.iloc[:,3].shape[0]
    if(lim1!=lim2):     #sprawdzenie czy Dane rzeczywiste i modelowe są tej samej długoci
        return -9 
    
    for i in range(lim):
        data=Data.iat[i,3]
        model=Model.iat[i,3]
        
        if (data==-9 or model==-9):        #odrzucenie danych które są równe -9           
            continue
        if(data<TH):
            data=TH
        if(model<TH):
            model=TH
            
        sumaCp+=model
        sumaCo+=data
        ilosc+=1
    
    sredniaCp=sumaCp/ilosc
    sredniaCo=sumaCo/ilosc
    print('srednia Co Cp ',sredniaCo,sredniaCp)
    for i in range(lim):
        data=Data.iat[i,3]
        model=Model.iat[i,3]
        
        if (data==-9 or model==-9):        #odrzucenie danych które są równe -9           
            continue
        if(data<TH):
            data=TH
        if(model<TH):
            model=TH
        
        qCp+=(model-sredniaCp)**2
        qCo+=(data-sredniaCo)**2
    
    qCp=m.sqrt(qCp/ilosc)
    qCo=m.sqrt(qCo/ilosc)    
    wynik=qCp/qCo
    return round(wynik,2)

def NRMSE(Model,Data,TH):
    lim=len(Model['Modeled values'])
    qCp=0
    qCo=0
    sredniaCp=0
    sredniaCo=0
    sumaCp=0
    sumaCo=0    
    
    
    data=0
    model=0
    ilosc=0
    lim1=Model.iloc[:,3].shape[0]
    lim2=Data.iloc[:,3].shape[0]
    if(lim1!=lim2):     #sprawdzenie czy Dane rzeczywiste i modelowe są tej samej długoci
        return -9 
    
    for i in range(lim):
        data=Data.iat[i,3]
        model=Model.iat[i,3]
        
        if (data==-9 or model==-9):        #odrzucenie danych które są równe -9           
            continue
        if(data<TH):
            data=TH
        if(model<TH):
            model=TH
            
        sumaCp+=model
        sumaCo+=data
        ilosc+=1
    
    sredniaCp=sumaCp/ilosc
    sredniaCo=sumaCo/ilosc
    NRMSE=0
    
    for i in range(lim):
        data=Data.iat[i,3]
        model=Model.iat[i,3]
        
        if (data==-9 or model==-9):        #odrzucenie danych które są równe -9           
            continue
        if(data<TH):
            data=TH
        if(model<TH):
            model=TH
        
        NRMSE+=((model-sredniaCp)-(data-sredniaCp))**2
        qCp+=(model-sredniaCp)**2
        qCo+=(data-sredniaCo)**2
    
    qCo=m.sqrt(qCo/ilosc)
    
    NRMSE=NRMSE/ilosc    
    NRMSE=m.sqrt(NRMSE)/qCo
    return round(NRMSE,2)

# def kontrola(Model1,Data1,TH):
#     lim1=Model1.iloc[:,3].shape[0]
#     lim2=Data1.iloc[:,3].shape[0]
#     tab1=[0 for i in range(10000)]      #Model
#     licznik=0
#     tab2=[0 for i in range(10000)]      #Data
    
#     if(lim1!=lim2):
#         return -9
#     for i in range(lim1):
#         if(Model1.iat[i,3]!=-9 & Data1.iat[i,3]!=-9):
#             tab1[licznik]=Model1.iat[i,3]
#             tab2[licznik]=Data1.iat[i,3]
#             licznik+=1
#     Model=[0 for i in range(licznik)]
#     Data=[0 for i in range(licznik)]
#     for i in range(licznik):
#         Model1[]    
                
#     return 1
        


Data= pd.read_csv('ASP01.txt', header =1, sep='\s*[;]\s*', index_col=False )             #Dane rzeczywiste 
Model = pd.read_csv('ASP01_MODEL-C.txt', header =1, sep='\s*[;]\s*',index_col=False )   #Dane modelowe

#print(Data)             sep='\s*[;]\s*'
#print(Data.iat[0,3])
#print(Model.dtypes)
#print(Model.iloc[0:7,0:7])
paths=['ASP01.txt','ASP01_MODEL-A.txt','ASP01_MODEL-B.txt','ASP01_MODEL-C.txt','ASP02.txt','ASP02_MODEL-A.txt','ASP02_MODEL-B.txt','ASP02_MODEL-C.txt'] 


#print('Współczynnik FB=  ',FB(Model,Data,50))
#print('Współczynnik FBFN=',FBFN(Model,Data))
#print('Współczynnik FBFP=',FBFP(Model,Data))
#print('Sprawdzenie FB=FBFN-FBFP= ',FBFN(Model,Data)-FBFP(Model,Data))
#print('Współczynnik MG=  ',MG(Model,Data))
#print('Współczynnik NMSE=',NMSE(Model,Data,0))
#print('Współczynnik R=   ',R(Model,Data,0))
#print('Współczynnik VG=  ', VG(Model,Data,50))
#print('Współczynnik FACX=',FACX(Model, Data, 2,50))
#print('Współczynnik NSD= ',NSD(Model, Data, 0))
print('Współczynnik NRMSE=',NRMSE(Model, Data, 0))
print('-------------------')
FractionalBiasFBdiagram(paths, 2, 3,0)
quantilpaths=['ASP01.txt','ASP01_MODEL-A.txt','ASP01_MODEL-B.txt','ASP01_MODEL-C.txt']
#quantile_quantile_plots(quantilpaths)
#MGandVG(paths, 1, 3,50)


