def validar_fecha():
    while True:
        dia=""
        while True:
            if dia=="":
                try:
                    dia=int(input("\nDigite el día (##) (y a continuación oprima la tecla 'enter'): " ))
                except ValueError as err:
                    print("\nIngreso incorrecto.")
            else:
                break
        mes=""
        while True:
            if mes=="":
                try:
                    mes=int(input("\nDigite el mes (##) (y a continuación oprima la tecla 'enter'): " ))
                except ValueError as err:
                    print("\nIngreso incorrecto.")
            else:
                break
        año=""
        while True:
            if año=="":
                try:
                    año=int(input("\nDigite el año (####) (y a continuación oprima la tecla 'enter'): " ))
                except ValueError as err:
                    print("\nIngreso incorrecto.")
            else:
                break
        mod4=año%4
        mod100=año%100
        mod400=año%400
        if mod4==0:
            if mod100==0:
                if mod400==0:
                    bisiesto=True
                else:
                    bisiesto=False
            else:
                bisiesto=True
        else:
            bisiesto=False
        if bisiesto==True and año>=1900 and año<2101:
            if mes==2:
                if dia>0 and dia<30:
                    break
                else:
                    print("\nFecha incorrecta, intente nuevamente")
            elif mes==4 or mes==6 or mes==9 or mes==11:
                if dia>0 and dia<31:
                    break
                else:
                    print("\nFecha incorrecta, intente nuevamente")
            elif mes==1 or mes==3 or mes==5 or mes==7 or mes==8 or mes==10 or mes==12:
                if dia>0 and dia<32:
                    break
                else:
                    print("\nFecha incorrecta, intente nuevamente")
            else:
                print("\nFecha incorrecta, intente nuevamente")
        elif bisiesto==False and año>=1900 and año<2101:
            if mes==2:
                if dia>0 and dia<29:
                    break
                else:
                    print("\nFecha incorrecta, intente nuevamente")
            elif mes==4 or mes==6 or mes==9 or mes==11:
                if dia>0 and dia<31:
                    break
                else:
                    print("\nFecha incorrecta, intente nuevamente")
            elif mes==1 or mes==3 or mes==5 or mes==7 or mes==8 or mes==10 or mes==12:
                if dia>0 and dia<32:
                    break
                else:
                    print("\nFecha incorrecta, intente nuevamente")
            else:
                print("\nFecha incorrecta, intente nuevamente")
        else:
            print("\nFecha incorrecta, intente nuevamente")
    return (dia, mes, año, bisiesto)
def numero_diasf(me):
    cont=d=0
    for i in range (me):
        if i==2:
            d=28
        elif i==4 or i==6 or i==9 or i==11:
            d=30
        elif i==1 or i==3 or i==5 or i==7 or i==8 or i==10 or i==12:
            d=31
        cont=cont+d
    return(cont)
def numero_diast(me):
    cont=d=0
    for i in range (me):
        if i==2:
            d=29
        elif i==4 or i==6 or i==9 or i==11:
            d=30
        elif i==1 or i==3 or i==5 or i==7 or i==8 or i==10 or i==12:
            d=31
        cont=cont+d
    return(cont)
def suma1():
    parcial3=0
    for i in range(fesol[2],fecit[2],1):
        mod4=i%4
        mod100=i%100
        mod400=i%400
        if mod4==0:
            if mod100==0:
                if mod400==0:                    #bisiesto=True
                    if i==fesol[2]:
                        parcial2=numero_diast(fesol[1])
                        parcial3=367-parcial2-fesol[0]
                    else:
                        parcial3=366+parcial3
                else:                    #bisiesto=False
                    if i==fesol[2]:
                        parcial2=numero_diasf(fesol[1])
                        parcial3=366-parcial2-fesol[0]
                    else:
                        parcial3=365+parcial3
            else:                #bisiesto=True
                if i==fesol[2]:
                    parcial2=numero_diast(fesol[1])
                    parcial3=367-parcial2-fesol[0]
                else:
                    parcial3=366+parcial3
        else:            #bisiesto=False
            if i==fesol[2]:
                parcial2=numero_diasf(fesol[1])
                parcial3=366-parcial2-fesol[0]
            else:
                parcial3=365+parcial3
    return(parcial3)
def suma2():
    parcial3=0
    for i in range(fecit[2],feent[2],1):
        mod4=i%4
        mod100=i%100
        mod400=i%400
        if mod4==0:
            if mod100==0:
                if mod400==0:                    #bisiesto=True
                    if i==fecit[2]:
                        parcial2=numero_diast(fecit[1])
                        parcial3=367-parcial2-fecit[0]
                    else:
                        parcial3=366+parcial3
                else:                    #bisiesto=False
                    if i==fecit[2]:
                        parcial2=numero_diasf(fecit[1])
                        parcial3=366-parcial2-fecit[0]
                    else:
                        parcial3=365+parcial3
            else:                #bisiesto=True
                if i==fecit[2]:
                    parcial2=numero_diast(fecit[1])
                    parcial3=367-parcial2-fecit[0]
                else:
                    parcial3=366+parcial3
        else:            #bisiesto=False
            if i==fecit[2]:
                parcial2=numero_diasf(fecit[1])
                parcial3=366-parcial2-fecit[0]
            else:
                parcial3=365+parcial3
    return(parcial3)
print("\nLaboratorio Clínico del Sur")
print("\nRevisión fechas de atención de pacientes.")
listado=["\nPACIENTES CON TIEMPOS DE ESPERA SUPERIORES A LO ESTABLECIDO\n"]
salida=""
while salida!="salir":
    print("\nIngrese los datos del paciente a continuación:")
    print("\n↓ Fecha de solicitud de la cita ↓")
    fesol=validar_fecha()
    print("\n↓ Fecha de la cita ↓")
    while True:
        fecit=validar_fecha()
        if fecit[2]>fesol[2]:
            parci3=suma1()
            if fecit[3]==False:    
                parcial=numero_diasf(fecit[1])
                parcial=parcial+fecit[0]
            elif fecit[3]==True:   
                parcial=numero_diast(fecit[1])
                parcial=parcial+fecit[0]
            tot=parcial+parci3
            break
        elif fecit[2]==fesol[2]:
            if fecit[1]>fesol[1]:
                if fecit[3]==False:    
                    parcial=numero_diasf(fecit[1])
                    parcial=parcial+fecit[0]    
                    parcial4=numero_diasf(fesol[1])
                    parcial4=parcial4+fesol[0]
                elif fecit[3]==True:   
                    parcial=numero_diast(fecit[1])
                    parcial=parcial+fecit[0]
                    parcial4=numero_diast(fesol[1])
                    parcial4=parcial4+fesol[0]
                tot=parcial-parcial4+1
                break
            elif fecit[1]==fesol[1]:
                if fecit[0]>=fesol[0]:
                    if fecit[3]==False:    
                        parcial=numero_diasf(fecit[1])
                        parcial=parcial+fecit[0]
                        parcial4=numero_diasf(fesol[1])
                        parcial4=parcial4+fesol[0]
                    elif fecit[3]==True:   
                        parcial=numero_diast(fecit[1])
                        parcial=parcial+fecit[0]
                        parcial4=numero_diast(fesol[1])
                        parcial4=parcial4+fesol[0]
                    tot=parcial-parcial4+1
                    break
                else:
                    print("\nFecha incorrecta, la fecha de la cita no puede ser anterior a la fecha de solicitud, intente nuevamente")
            else:
                print("\nFecha incorrecta, la fecha de la cita no puede ser anterior a la fecha de solicitud, intente nuevamente")
        else:
            print("\nFecha incorrecta, la fecha de la cita no puede ser anterior a la fecha de solicitud, intente nuevamente")
    print("\n↓ Fecha de entrega de muestras ↓")
    while True:
        feent=validar_fecha()
        if feent[2]>fecit[2]:
            parci3=suma2()
            if feent[3]==False:    
                parcial=numero_diasf(feent[1])
                parcial=parcial+feent[0]
            elif feent[3]==True:   
                parcial=numero_diast(feent[1])
                parcial=parcial+feent[0]
            tot2=parcial+parci3
            break
        elif feent[2]==fecit[2]:
            if feent[1]>fecit[1]:
                if feent[3]==False:    
                    parcial=numero_diasf(feent[1])
                    parcial=parcial+feent[0]
                    parcial4=numero_diasf(fecit[1])
                    parcial4=parcial4+fecit[0]            
                elif feent[3]==True:   
                    parcial=numero_diast(feent[1])
                    parcial=parcial+feent[0]   
                    parcial4=numero_diast(fecit[1])
                    parcial4=parcial4+fecit[0]
                tot2=parcial-parcial4+1
                break
            elif feent[1]==fecit[1]:
                if feent[0]>=fecit[0]:
                    if feent[3]==False:    
                        parcial=numero_diasf(feent[1])
                        parcial=parcial+feent[0] 
                        parcial4=numero_diasf(fecit[1])
                        parcial4=parcial4+fecit[0]
                    elif feent[3]==True:   
                        parcial=numero_diast(feent[1])
                        parcial=parcial+feent[0]
                        parcial4=numero_diast(fecit[1])
                        parcial4=parcial4+fecit[0]
                    tot2=parcial-parcial4+1
                    break
                else:
                    print("\nFecha incorrecta, la fecha de la entrega de muestras no puede ser anterior a la fecha de la cita, intente nuevamente")
            else:
                print("\nFecha incorrecta, la fecha de la entrega de muestras no puede ser anterior a la fecha de la cita, intente nuevamente")
        else:
            print("\nFecha incorrecta, la fecha de la entrega de muestras no puede ser anterior a la fecha de la cita, intente nuevamente")
    nombre=""
    while True:
        if nombre=="":
            nombre=input("\nDigite el nombre completo del paciente (y a continuación oprima la tecla 'enter'): " ).strip().title()
        else:
            break
    documento=""
    while True:
        if documento=="":
            documento=input("\nDigite el número de documento del paciente (y a continuación oprima la tecla 'enter'): " ).strip().title()
        else:
            break
    telefono=""
    while True:
        if telefono=="":
            telefono=input("\nDigite el teléfono de contacto (y a continuación oprima la tecla 'enter'): " ).strip().title()
        else:
            break
    tot=tot-1
    tot2=tot2-1
    if tot>=3 or tot2>=4:
        listado.append(str(len(listado))+") "+nombre+" - "+str(tot)+" días entre llamada y cita, "+str(tot2)+" días entre cita y resultados - Teléfono: "+telefono+"\n")
    salida=""
    while True:
        if salida=="S" or salida=="s" or salida=="si" or salida=="SI":
            break
        elif salida=="N" or salida=="n" or salida=="no" or salida=="NO":
            salida="salir"
            break
        else:
            salida=input("\n¿Desea agregar los datos de otro paciente? (S/N): ")
for i in range(len(listado)):
        print(listado[i])
print("Total de pacientes con tiempos superiores: "+str(len(listado)-1)+"\n")