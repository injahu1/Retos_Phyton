print("\nTu Nueva Casa S.A.S.")
salida=""
while salida!="salir":
    print("\n↓ Ingrese los datos de 5 cotizaciones ↓")
    cotiza=(["Primera cotización:"], ["Segunda cotización:"], ["Tercera cotización:"],["Cuarta cotización:"], ["Quinta cotización:"])
    for i in range (5):
        print("\n"+cotiza[i][0])
        nit=""
        while True:
            try:
                nit=int(input("\nIngrese NIT de la empresa (y a continuación oprima la tecla 'enter'): "))
            except ValueError as err:
                print("\nIngreso incorrecto, intente nuevamente")
            else:
                if (10**49)>nit>0:
                    break
                else:
                    print("\nIngreso incorrecto, intente nuevamente")
        nombre=""
        while True:
            if nombre=="":
                nombre=input("\nNombre de la empresa (y a continuación oprima la tecla 'enter'): " )
            else:
                break
        valor=""
        while True:
            try:
                valor=float(input("\nDigite el monto total de la cotización (y a continuación oprima la tecla 'enter'): "))
            except ValueError as err:
                print("\nIngreso incorrecto, intente nuevamente")
            else:
                if (10**49)>valor>0:
                    break
                else:
                    print("\nIngreso incorrecto, intente nuevamente")
        cotiza[i].append(nit)
        cotiza[i].append(nombre)
        cotiza[i].append(valor)
    print("\n--------------------------------------------------------------------------------------")
    suma=0
    compare=0
    for j in range (5):
        suma=(float(cotiza[j][3])+ suma)
        if cotiza[j][3]>=compare:
            indma=cotiza[j][0]
            nitma=cotiza[j][1]
            nomma=cotiza[j][2]
            compare=cotiza[j][3]
            compare2=compare
    for j in range (4,-1,-1):
        if cotiza[j][3]<=compare2:
            indme=cotiza[j][0]
            nitme=cotiza[j][1]
            nomme=cotiza[j][2]
            compare2=cotiza[j][3]
    promedio =suma/5
    print("\nCotización más baja")
    print("\nNIT: "+str(nitme))
    print("\nNombre: "+(nomme).title().strip())
    print("\nValor: "+str(compare2))
    print("\n\n\nCotización más alta")
    print("\nNIT: "+str(nitma))
    print("\nNombre: "+(nomma).title().strip())
    print("\nValor: "+str(compare))
    print("\n\n\nPromedio: "+str(promedio)+"\n")
    salida=""
    while True:
        if salida=="S" or salida=="s" or salida=="si" or salida=="SI":
            break
        elif salida=="N" or salida=="n" or salida=="no" or salida=="NO":
            salida="salir"
            break
        else:
            salida=input("\n¿Desea realizar una nueva sesión de cotizaciones? (S/N): ")
            print("\n")