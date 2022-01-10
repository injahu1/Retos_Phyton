print("Clínica Dental Sonrisas Blancas S.A")
print("\nBienvenido")
print("\nEsta herramienta permite crear una ficha de caracterización de los pacientes a los que les han realizado procedimientos de topicación de flúor en barniz")
nombres=""
while True:
    if nombres=="":
        nombres=input("\nDigite los nombres del paciente (y a continuación oprima la tecla 'enter'): " )
    else:
        break
apellido=""
while True:
    if apellido=="":
        apellido=input("\nDigite los apellidos del paciente (y a continuación oprima la tecla 'enter'): " )
    else:
        break
direccion=""
while True:
    if direccion=="":
        direccion=input("\nDigite la dirección de residencia (y a continuación oprima la tecla 'enter'): " )
    else:
        break
telefono=""
while True:
    if telefono=="":
        telefono=input("\nDigite el teléfono de contacto (y a continuación oprima la tecla 'enter'): " )
    else:
        break
sexo=""
a=0
while True:
    if sexo=="F" or sexo=="f" or sexo=="Femenino" or sexo=="M" or sexo=="m" or sexo=="Masculino":
        if sexo=="F" or sexo=="f" or sexo=="Femenino":
            sexo="Femenino"
        else:
            sexo="Masculino"
        break
    else:
        if a>0:
            print("\nIngreso incorrecto.")
        a=1
        sexo=input("\nDigite el sexo (Femenino o Masculino) (F/M) (y a continuación oprima la tecla 'enter'): " )
while True:
    print("\n↓ Fecha de nacimiento ↓")
    dianac=""
    while True:
        if dianac=="":
            try:
                dianac=int(input("\nDigite el día (##) (y a continuación oprima la tecla 'enter'): " ))
            except ValueError as err:
                print("\nIngreso incorrecto.")
        else:
            break
    mesnac=""
    while True:
        if mesnac=="":
            try:
                mesnac=int(input("\nDigite el mes (##) (y a continuación oprima la tecla 'enter'): " ))
            except ValueError as err:
                print("\nIngreso incorrecto.")
        else:
            break
    añonac=""
    while True:
        if añonac=="":
            try:
                añonac=int(input("\nDigite el año (####) (y a continuación oprima la tecla 'enter'): " ))
            except ValueError as err:
                print("\nIngreso incorrecto.")
        else:
            break
    mod4=añonac%4
    mod100=añonac%100
    mod400=añonac%400
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
    if bisiesto==True and añonac>=1900 and añonac<2101:
        if mesnac==2:
            if dianac>0 and dianac<30:
                break
            else:
                print("\nFecha incorrecta, intente nuevamente")
        elif mesnac==4 or mesnac==6 or mesnac==9 or mesnac==11:
            if dianac>0 and dianac<31:
                break
            else:
                print("\nFecha incorrecta, intente nuevamente")
        elif mesnac==1 or mesnac==3 or mesnac==5 or mesnac==7 or mesnac==8 or mesnac==10 or mesnac==12:
            if dianac>0 and dianac<32:
                break
            else:
                print("\nFecha incorrecta, intente nuevamente")
        else:
            print("\nFecha incorrecta, intente nuevamente")
    elif bisiesto==False and añonac>=1900 and añonac<2101:
        if mesnac==2:
            if dianac>0 and dianac<29:
                break
            else:
                print("\nFecha incorrecta, intente nuevamente")
        elif mesnac==4 or mesnac==6 or mesnac==9 or mesnac==11:
            if dianac>0 and dianac<31:
                break
            else:
                print("\nFecha incorrecta, intente nuevamente")
        elif mesnac==1 or mesnac==3 or mesnac==5 or mesnac==7 or mesnac==8 or mesnac==10 or mesnac==12:
            if dianac>0 and dianac<32:
                break
            else:
                print("\nFecha incorrecta, intente nuevamente")
        else:
            print("\nFecha incorrecta, intente nuevamente")
    else:
        print("\nFecha incorrecta, intente nuevamente")
while True:
    print("\n↓ Fecha de realización del procedimiento ↓")
    fnvalida=False
    diapro=""
    while True:
        if diapro=="":
            try:
                diapro=int(input("\nDigite el día (##) (y a continuación oprima la tecla 'enter'): " ))
            except ValueError as err:
                print("\nIngreso incorrecto.")
        else:
            break
    mespro=""
    while True:
        if mespro=="":
            try:
                mespro=int(input("\nDigite el mes (##) (y a continuación oprima la tecla 'enter'): " ))
            except ValueError as err:
                print("\nIngreso incorrecto.")
        else:
            break
    añopro=""
    while True:
        if añopro=="":
            try:
                añopro=int(input("\nDigite el año (####) (y a continuación oprima la tecla 'enter'): " ))
            except ValueError as err:
                print("\nIngreso incorrecto.")
        else:
            break
    m4=añopro%4
    m100=añopro%100
    m400=añopro%400
    if m4==0:
        if m100==0:
            if m400==0:
                bisiesto2=True
            else:
                bisiesto2=False
        else:
            bisiesto2=True
    else:
        bisiesto2=False
    if bisiesto2==True and añopro>=1900 and añopro<2101:
        if mespro==2:
            if diapro>0 and diapro<30:
                fnvalida=True#break
            else:
                print("\nFecha incorrecta, intente nuevamente")
        elif mespro==4 or mespro==6 or mespro==9 or mespro==11:
            if diapro>0 and diapro<31:
                fnvalida=True#break
            else:
                print("\nFecha incorrecta, intente nuevamente")
        elif mespro==1 or mespro==3 or mespro==5 or mespro==7 or mespro==8 or mespro==10 or mespro==12:
            if diapro>0 and diapro<32:
                fnvalida=True#break
            else:
                print("\nFecha incorrecta, intente nuevamente")
        else:
            print("\nFecha incorrecta, intente nuevamente")
    elif bisiesto2==False and añopro>=1900 and añopro<2101:
        if mespro==2:
            if diapro>0 and diapro<29:
                fnvalida=True#break
            else:
                print("\nFecha incorrecta, intente nuevamente")
        elif mespro==4 or mespro==6 or mespro==9 or mespro==11:
            if diapro>0 and diapro<31:
                fnvalida=True#break
            else:
                print("\nFecha incorrecta, intente nuevamente")
        elif mespro==1 or mespro==3 or mespro==5 or mespro==7 or mespro==8 or mespro==10 or mespro==12:
            if diapro>0 and diapro<32:
                fnvalida=True#break
            else:
                print("\nFecha incorrecta, intente nuevamente")
        else:
            print("\nFecha incorrecta, intente nuevamente")
    else:
        print("\nFecha incorrecta, intente nuevamente")
    if fnvalida==True:
        if añopro>añonac:
            if mespro>mesnac:
                edad=añopro-añonac
                break
            elif mespro==mesnac:
                if diapro>=dianac:
                    edad=añopro-añonac
                    break
                else:
                    edad=añopro-añonac-1
                    break
            else:
                edad=añopro-añonac-1
                break
        elif añopro==añonac:
            if mespro>mesnac:
                edad=0
                break
            elif mespro==mesnac:
                if diapro>=dianac:
                    edad=0
                    break
                else:
                    print("\nFecha incorrecta, la fecha del procedimiento no puede ser anterior a la fecha de nacimiento, intente nuevamente")
            else:
                print("\nFecha incorrecta, la fecha del procedimiento no puede ser anterior a la fecha de nacimiento, intente nuevamente")
        else:
            print("\nFecha incorrecta, la fecha del procedimiento no puede ser anterior a la fecha de nacimiento, intente nuevamente")    
if 0<=edad<=5:
    ciclo="Primera infancia"
elif 6<=edad<=11:
    ciclo="Infancia"
elif 12<=edad<=18:
    ciclo="Adolescencia"
elif 19<=edad<=26:
    ciclo="Juventud"
elif 27<=edad<=59:
    ciclo="Adultez"
else:
    ciclo="Persona mayor"
if edad<56:
    medad=edad%5
    if medad==0:
        segui="Es necesario seguimiento detallado por edad"
    else:
        segui="No es necesario seguimiento detallado por edad"
else:
    segui="No es necesario seguimiento detallado por edad"
print("\nNombre: " + (nombres + " " + apellido).title())
print("\nDirección de residencia: " + direccion)
print("\nTeléfono: " + telefono)
print("\nSexo: " + sexo)
print("\nEdad: " + str(edad) + " años")
print("\nCiclo vital: " + ciclo)
print("\n" + segui+ "\n")