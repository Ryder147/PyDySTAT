import math as m

#geometric variance    
def VG(sensor_out_model, sensor_exp, TH):
    suma=0
    data=0
    model=0
    ilosc=0

    lim = len(sensor_out_model.sim_values)
    lim_tmp = len(sensor_exp.measurement)
    
    if(lim != lim_tmp):     #sprawdzenie czy Dane rzeczywiste i modelowe są tej samej długoci
        return -9
    
    for i in range(lim):
        data = sensor_exp.measurement[i]
        model = sensor_out_model.sim_values[i]
        
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
def FACX(sensor_out_model, sensor_exp, x, TH):         
    licznik=0
    data=0
    model=0
    wynik=0
    
    lim = len(sensor_out_model.sim_values)
    lim_tmp = len(sensor_exp.measurement)
    
    if(lim != lim_tmp):     #sprawdzenie czy Dane rzeczywiste i modelowe są tej samej długoci
        return -9
    
    for i in range(lim):
        data = sensor_exp.measurement[i]
        model = sensor_out_model.sim_values[i]
        
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
def FB(sensor_out_model, sensor_exp, TH):     
    data=0
    model=0
    ilosc=0
    
    lim = len(sensor_out_model.sim_values)
    lim_tmp = len(sensor_exp.measurement)
    
    if(lim != lim_tmp):     #sprawdzenie czy Dane rzeczywiste i modelowe są tej samej długoci
        return -9    
    
    sCo=float(0.0)          
    sCp=float(0.0)          
    for i in range(lim):
        data = sensor_exp.measurement[i]
        model = sensor_out_model.sim_values[i]
        
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
def FBFN(sensor_out_model, sensor_exp, TH):           
    suma1=0
    suma2=0
    
    data=0
    model=0
    
    lim = len(sensor_out_model.sim_values)
    lim_tmp = len(sensor_exp.measurement)
    
    if(lim !=lim_tmp):     #sprawdzenie czy Dane rzeczywiste i modelowe są tej samej długoci
        return -9 
    
    for i in range(lim):
        data = sensor_exp.measurement[i]
        model = sensor_out_model.sim_values[i]
        
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
def FBFP(sensor_out_model, sensor_exp, TH):           
    suma1=0
    suma2=0   
    
    data=0
    model=0
    
    lim = len(sensor_out_model.sim_values)
    lim_tmp = len(sensor_exp.measurement)
    
    if(lim != lim_tmp):     #sprawdzenie czy Dane rzeczywiste i modelowe są tej samej długoci
        return -9 
    
    for i in range(lim):
        data = sensor_exp.measurement[i]
        model = sensor_out_model.sim_values[i]
        
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
def MG(sensor_out_model, sensor_exp, TH):         
    slnCo=0
    slnCp=0
    
    data=0
    model=0
    ilosc=0
    
    lim = len(sensor_out_model.sim_values)
    lim_tmp = len(sensor_exp.measurement)
    
    if(lim != lim_tmp):     #sprawdzenie czy Dane rzeczywiste i modelowe są tej samej długoci
        return -9 
    
    for i in range(lim):
        data = sensor_exp.measurement[i]
        model = sensor_out_model.sim_values[i]
        
        if (data==-9 or model==-9):        #odrzucenie danych które są równe -9           
            continue
        if(data<TH):
            data=TH
        if(model<TH):
            model=TH
            
        slnCo+=m.log(data)
        slnCp+=m.log(model)
        ilosc+=1
        
    slnCp=slnCp/ilosc
    slnCo=slnCo/ilosc
    
    MG=m.exp(slnCo-slnCp)
    return round(MG,2)

#normalized mean square error
def NMSE(sensor_out_model, sensor_exp, TH):          
    sCo=float(0.0)          
    sCp=float(0.0)
    suma=0
         
    data=0
    model=0
    ilosc=0
    
    lim = len(sensor_out_model.sim_values)
    lim_tmp = len(sensor_exp.measurement)
    
    if(lim != lim_tmp):     #sprawdzenie czy Dane rzeczywiste i modelowe są tej samej długoci
        return -9 
    
    for i in range(lim):
        data = sensor_exp.measurement[i]
        model = sensor_out_model.sim_values[i]
        
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
def R(sensor_out_model, sensor_exp, TH):
    sCo=float(0.0)          
    sCp=float(0.0)  
        
    data=0
    model=0
    ilosc=0
    
    lim = len(sensor_out_model.sim_values)
    lim_tmp = len(sensor_exp.measurement)
    
    if(lim != lim_tmp):     #sprawdzenie czy Dane rzeczywiste i modelowe są tej samej długoci
        return -9 
    
    for i in range(lim):
        data = sensor_exp.measurement[i]
        model = sensor_out_model.sim_values[i]
        
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
    
    for i in range(lim):
        data = sensor_exp.measurement[i]
        model = sensor_out_model.sim_values[i]
        
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
def NSD(sensor_out_model, sensor_exp, TH):
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
    
    lim = len(sensor_out_model.sim_values)
    lim_tmp = len(sensor_exp.measurement)
    
    if(lim != lim_tmp):     #sprawdzenie czy Dane rzeczywiste i modelowe są tej samej długoci
        return -9 
    
    for i in range(lim):
        data = sensor_exp.measurement[i]
        model = sensor_out_model.sim_values[i]
        
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
        data = sensor_exp.measurement[i]
        model = sensor_out_model.sim_values[i]
        
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
def NRMSE(sensor_out_model, sensor_exp, TH):
    qCp=0
    qCo=0
    sredniaCp=0
    sredniaCo=0
    sumaCp=0
    sumaCo=0    
    
    data=0
    model=0
    ilosc=0
    
    lim = len(sensor_out_model.sim_values)
    lim_tmp = len(sensor_exp.measurement)
    
    if(lim != lim_tmp):                        #sprawdzenie czy Dane rzeczywiste i modelowe są tej samej długoci
        return -9 
    
    for i in range(lim):
        data = sensor_exp.measurement[i]
        model = sensor_out_model.sim_values[i]
        
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
        data = sensor_exp.measurement[i]
        model = sensor_out_model.sim_values[i]
        
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
def Afn(sensor_out_model, sensor_exp, TH):
    Afn=0
    suma=0
    data=0
    model=0
   
    lim = len(sensor_out_model.sim_values)
    lim_tmp = len(sensor_exp.measurement)
    
    if(lim != lim_tmp):                        #sprawdzenie czy Dane rzeczywiste i modelowe są tej samej długoci
        return -9 
    
    for i in range(lim):
        data = sensor_exp.measurement[i]
        model = sensor_out_model.sim_values[i]
        
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
def Afp(sensor_out_model, sensor_exp, TH):    
    Afp=0
    suma=0
    data=0
    model=0
   
    lim = len(sensor_out_model.sim_values)
    lim_tmp = len(sensor_exp.measurement)
    
    if(lim != lim_tmp):                        #sprawdzenie czy Dane rzeczywiste i modelowe są tej samej długoci
        return -9 
    
    for i in range(lim):
        data = sensor_exp.measurement[i]
        model = sensor_out_model.sim_values[i]
        
        if (data==-9 or model==-9):        #odrzucenie danych które są równe -9           
            continue
        if(data<TH):
            data=TH
        if(model<TH):
            model=TH
        suma+=m.fabs(data-model)+(model-data)
        
    Afp=(1/2)*suma
    return round(Afp,2)

def iloczynApAo(sensor_out_model, sensor_exp, TH):
    ApAo=0
    suma=0
    data=0
    model=0
   
    lim = len(sensor_out_model.sim_values)
    lim_tmp = len(sensor_exp.measurement)
    
    if(lim != lim_tmp):                        #sprawdzenie czy Dane rzeczywiste i modelowe są tej samej długoci
        return -9
    
    for i in range(lim):
        data = sensor_exp.measurement[i]
        model = sensor_out_model.sim_values[i]
        
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
def FMS(sensor_out_model, sensor_exp, TH):
    fms=(iloczynApAo(sensor_out_model, sensor_exp, TH))/(iloczynApAo(sensor_out_model, sensor_exp, TH)+Afn(sensor_out_model, sensor_exp, TH)+Afp(sensor_out_model, sensor_exp, TH))
    return round(fms,2)
    
    return 1
# measure of effectivness (false negative)
def MOEfn(sensor_out_model, sensor_exp, TH):
    MOEFN=(2-FBFN(sensor_out_model, sensor_exp, TH)-FBFP(sensor_out_model, sensor_exp, TH))/(2+FB(sensor_out_model, sensor_exp, TH))
    return round(MOEFN,2)

# measure of effectivness (false positive)
def MOEfp(sensor_out_model, sensor_exp, TH):
    MOEFP=(2-FBFN(sensor_out_model, sensor_exp, TH)-FBFP(sensor_out_model, sensor_exp, TH))/(2-FB(sensor_out_model, sensor_exp, TH))
    return round(MOEFP,2)