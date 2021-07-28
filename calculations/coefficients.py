
import numpy as np
import pandas as pd
import math as m
import matplotlib.pyplot as plt
import matplotlib





#geometric variance    
def VG(Model,Data,TH):          
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

#fraction of predictions X        
def FACX(Model,Data,x,TH):         
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


#fractional bias
def FB(Model,Data,TH):             
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

    
#fractional bias false negative
def FBFN(Model,Data,TH):           
    
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

#fractional bias false positive
def FBFP(Model,Data,TH):           
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

#geometric mean bias
def MG(Model,Data,TH):         
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


#normalized mean square error
def NMSE(Model, Data,TH):          
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

#correlation coefficient
def R(Model,Data,TH):          
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

# normalized standard deviation
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


# normalized root mean square error
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
    if(lim1!=lim2):                        #sprawdzenie czy Dane rzeczywiste i modelowe są tej samej długoci
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
# area of ‘‘false negative’’ predictions
def Afn(Model,Data,TH):
    
    lim=len(Model['Modeled values'])   
    
    Afn=0
    suma=0
    data=0
    model=0
   
    lim1=Model.iloc[:,3].shape[0]
    lim2=Data.iloc[:,3].shape[0]
    if(lim1!=lim2):                        #sprawdzenie czy Dane rzeczywiste i modelowe są tej samej długoci
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
        suma+=m.fabs(data-model)+(data-model)
        
    Afn=(1/2)*suma
    return round(Afn,2)
  
# area of ‘‘false positive’’ predictions          
def Afp(Model,Data,TH):
    lim=len(Model['Modeled values'])   
    
    Afp=0
    suma=0
    data=0
    model=0
   
    lim1=Model.iloc[:,3].shape[0]
    lim2=Data.iloc[:,3].shape[0]
    if(lim1!=lim2):                        #sprawdzenie czy Dane rzeczywiste i modelowe są tej samej długoci
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
        suma+=m.fabs(data-model)+(model-data)
        
    Afp=(1/2)*suma
    return round(Afp,2)

def iloczynApAo(Model,Data,TH):
    lim=len(Model['Modeled values'])   
    
    ApAo=0
    suma=0
    data=0
    model=0
   
    lim1=Model.iloc[:,3].shape[0]
    lim2=Data.iloc[:,3].shape[0]
    if(lim1!=lim2):                        #sprawdzenie czy Dane rzeczywiste i modelowe są tej samej długoci
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
        suma+=(data+model)-m.fabs(data-model)-TH
        
    ApAo=(1/2)*suma
    return round(ApAo,2)

# figure of merit in space
def FMS(Model,Data,TH):
    fms=(iloczynApAo(Model,Data,TH))/(iloczynApAo(Model,Data,TH)+Afn(Model,Data,TH)+Afp(Model,Data,TH))
    return round(fms,2)
    
    return 1
# measure of effectivness (false negative)
def MOEfn(Model,Data,TH):
    MOEFN=(2-FBFN(Model, Data, TH)-FBFP(Model, Data, TH))/(2+FB(Model,Data,TH))
    return round(MOEFN,2)

# measure of effectivness (false positive)
def MOEfp(Model,Data,TH):
    MOEFP=(2-FBFN(Model, Data, TH)-FBFP(Model, Data, TH))/(2-FB(Model,Data,TH))    
    return round(MOEFP,2)

Data= pd.read_csv('ASP01.txt', header =1, sep='\s*[;]\s*', index_col=False )             #Dane rzeczywiste 
Model = pd.read_csv('ASP01_MODEL-C.txt', header =1, sep='\s*[;]\s*',index_col=False )   #Dane modelowe
Wind=pd.read_csv('MS01.txt', header =1, sep='\s*[;]\s*', index_col=False )


# print('Współczynnik FB=  ',FB(Model,Data,50))
# print('Współczynnik FBFN=',FBFN(Model,Data,0))
# print('Współczynnik FBFP=',FBFP(Model,Data,0))
# print('Sprawdzenie FB=FBFN-FBFP= ',FBFN(Model,Data,0)-FBFP(Model,Data,0))
# print('Współczynnik MG=  ',MG(Model,Data,0))
# print('Współczynnik NMSE=',NMSE(Model,Data,0))
# print('Współczynnik R=   ',R(Model,Data,0))
# print('Współczynnik VG=  ', VG(Model,Data,50))
# print('Współczynnik FACX=',FACX(Model, Data, 2,50))
# print('Współczynnik NSD= ',NSD(Model, Data, 0))
# print('Współczynnik NRMSE=',NRMSE(Model, Data, 0))
# print('Współczynnik Afn=  ',Afn(Model,Data,0))
# print('Współczynnik Afp=  ',Afp(Model,Data,0))
# print('Współczynnik FMS=  ',FMS(Model, Data, 0))
# print('Współczynnik MOEfn=',MOEfn(Model, Data, 0))
# print('Współczynnik MOEfp=',MOEfp(Model, Data, 0))
# print('Iloczyn Ap Ao =    ',iloczynApAo(Model, Data, 0))