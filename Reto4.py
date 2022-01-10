def pregunta():
    sali=""
    while True:
        if sali=="S" or sali=="s" or sali=="si" or sali=="SI":
            return True
        elif sali=="N" or sali=="n" or sali=="no" or sali=="NO":
            return False
        else:
            sali=input("\n¿Desea visualizar el listado? (S/N): ")
            print("\n")
print("\nONG Fundación Quindío Saludable")
try:
    archivo=open('Pacientes COVID-19 Quindío Mayo.csv', encoding='utf-8')
except FileNotFoundError:
    print("\nArchivo no encontrado")
    print("\nEl programa finaliza ahora\n")
else:
    lista=[]
    c=0
    for linea in archivo:
        if c>0:
            linea=linea.replace("\n","")
            l=linea.split(";")
            lista.append(l)  
        c+=1
    archivo.close()
    lcasos=[]
    lactivos=[]
    lfallecidos=[]
    lfemenino=[]
    lmasculino=[]
    lquinquenio=[]
    lquinqueniof=[]
    lq1=[]
    lq2=[]
    lq3=[]
    lq4=[]
    lq5=[]
    lq6=[]
    lq7=[]
    lq8=[]
    lq9=[]
    lq10=[]
    lq11=[]
    lq12=[]
    lq13=[]
    lq14=[]
    lq15=[]
    lq16=[]
    lq17=[]
    lqf1=[]
    lqf2=[]
    lqf3=[]
    lqf4=[]
    lqf5=[]
    lqf6=[]
    lqf7=[]
    lqf8=[]
    lqf9=[]
    lqf10=[]
    lqf11=[]
    lqf12=[]
    lqf13=[]
    lqf14=[]
    lqf15=[]
    lqf16=[]
    lqf17=[]
    lciudades=[]
    lcselect=[]
    lc1=[]
    lc2=[]
    lc3=[]
    lc4=[]
    lc5=[]
    lc6=[]
    lc7=[]
    lc8=[]
    lc9=[]
    lc10=[]
    lc11=[]
    lc12=[]
    lciudadest=[]
    lciudadestf=[]
    lcf1=[]
    lcf2=[]
    lcf3=[]
    lcf4=[]
    lcf5=[]
    lcf6=[]
    lcf7=[]
    lcf8=[]
    lcf9=[]
    lcf10=[]
    lcf11=[]
    lcf12=[]
    con=promedioef=0
    for i in range (len(lista)):
        lquinquenio=[lq1,lq2,lq3,lq4,lq5,lq6,lq7,lq8,lq9,lq10,lq11,lq12,lq13,lq14,lq15,lq16,lq17]
        lquinqueniof=[lqf1,lqf2,lqf3,lqf4,lqf5,lqf6,lqf7,lqf8,lqf9,lqf10,lqf11,lqf12,lqf13,lqf14,lqf15,lqf16,lqf17]
        edad=int(lista[i][4])
        posicion=edad//5
        if posicion>16:
            posicion=16
        if lista[i][7]=="Activo":
            lcasos.append(str(i+1)+". Notificado el "+lista[i][0]+" con código divipola: "+lista[i][1]+" en "+lista[i][2]+" | edad: "+lista[i][4]+" | sexo: "+lista[i][5]+" | estado: "+lista[i][7])
            lactivos.append(". Notificado el "+lista[i][0]+" con código divipola: "+lista[i][1]+" en "+lista[i][2]+" | edad: "+lista[i][4]+" | sexo: "+lista[i][5]+" | estado: "+lista[i][7])
            lquinquenio[posicion].append(". Notificado el "+lista[i][0]+" con código divipola: "+lista[i][1]+" en "+lista[i][2]+" | edad: "+lista[i][4]+" | sexo: "+lista[i][5]+" | estado: "+lista[i][7])
            if lista[i][5]=="M":
                lmasculino.append(". Notificado el "+lista[i][0]+" con código divipola: "+lista[i][1]+" en "+lista[i][2]+" | edad: "+lista[i][4]+" | sexo: "+lista[i][5]+" | estado: "+lista[i][7])
            elif lista[i][5]=="F":
                lfemenino.append(". Notificado el "+lista[i][0]+" con código divipola: "+lista[i][1]+" en "+lista[i][2]+" | edad: "+lista[i][4]+" | sexo: "+lista[i][5]+" | estado: "+lista[i][7])
        elif (lista[i][7]=="Fallecido") or (lista[i][9]!="\\N"):
            lcasos.append(str(i+1)+". Notificado el "+lista[i][0]+" con código divipola: "+lista[i][1]+" en "+lista[i][2]+" | edad: "+lista[i][4]+" | sexo: "+lista[i][5]+" | estado: "+lista[i][7]+" el día "+lista[i][9])
            lfallecidos.append(". Notificado el "+lista[i][0]+" con código divipola: "+lista[i][1]+" en "+lista[i][2]+" | edad: "+lista[i][4]+" | sexo: "+lista[i][5]+" | estado: "+lista[i][7]+" el día "+lista[i][9])
            lquinquenio[posicion].append(". Notificado el "+lista[i][0]+" con código divipola: "+lista[i][1]+" en "+lista[i][2]+" | edad: "+lista[i][4]+" | sexo: "+lista[i][5]+" | estado: "+lista[i][7]+" el día "+lista[i][9])
            lquinqueniof[posicion].append(". Notificado el "+lista[i][0]+" con código divipola: "+lista[i][1]+" en "+lista[i][2]+" | edad: "+lista[i][4]+" | sexo: "+lista[i][5]+" | estado: "+lista[i][7]+" el día "+lista[i][9])
            promedioef=(int(lista[i][4])+promedioef)
            if lista[i][5]=="M":
                lmasculino.append(". Notificado el "+lista[i][0]+" con código divipola: "+lista[i][1]+" en "+lista[i][2]+" | edad: "+lista[i][4]+" | sexo: "+lista[i][5]+" | estado: "+lista[i][7]+" el día "+lista[i][9])
            elif lista[i][5]=="F":
                lfemenino.append(". Notificado el "+lista[i][0]+" con código divipola: "+lista[i][1]+" en "+lista[i][2]+" | edad: "+lista[i][4]+" | sexo: "+lista[i][5]+" | estado: "+lista[i][7]+" el día "+lista[i][9])            
        elif lista[i][7]=="Recuperado":
            lcasos.append(str(i+1)+". Notificado el "+lista[i][0]+" con código divipola: "+lista[i][1]+" en "+lista[i][2]+" | edad: "+lista[i][4]+" | sexo: "+lista[i][5]+" | estado: "+lista[i][7]+" el día "+lista[i][8])
            lquinquenio[posicion].append(". Notificado el "+lista[i][0]+" con código divipola: "+lista[i][1]+" en "+lista[i][2]+" | edad: "+lista[i][4]+" | sexo: "+lista[i][5]+" | estado: "+lista[i][7]+" el día "+lista[i][8])
            if lista[i][5]=="M":
                lmasculino.append(". Notificado el "+lista[i][0]+" con código divipola: "+lista[i][1]+" en "+lista[i][2]+" | edad: "+lista[i][4]+" | sexo: "+lista[i][5]+" | estado: "+lista[i][7]+" el día "+lista[i][8])
            elif lista[i][5]=="F":
                lfemenino.append(". Notificado el "+lista[i][0]+" con código divipola: "+lista[i][1]+" en "+lista[i][2]+" | edad: "+lista[i][4]+" | sexo: "+lista[i][5]+" | estado: "+lista[i][7]+" el día "+lista[i][8])
        lciudades.append(lista[i][2])
    promedioef=promedioef/(len(lfallecidos))    
    lciudades.sort()
    for i in range(len(lciudades)):
        if con==0:
            lcselect.append(lciudades[i])
        if con>0:
            if lciudades[i]!=lciudades[i-1]:
                lcselect.append(lciudades[i])
        con+=1
    lciudadest=[lc1,lc2,lc3,lc4,lc5,lc6,lc7,lc8,lc9,lc10,lc11,lc12]
    lciudadestf=[lcf1,lcf2,lcf3,lcf4,lcf5,lcf6,lcf7,lcf8,lcf9,lcf10,lcf11,lcf12]
    for i in range (len(lcselect)):
        for j in range (len(lista)):
            if (lcselect[i])==(lista[j][2]):
                if lista[j][7]=="Activo":
                    lciudadest[i].append(". Notificado el "+lista[j][0]+" con código divipola: "+lista[j][1]+" en "+lista[j][2]+" | edad: "+lista[j][4]+" | sexo: "+lista[j][5]+" | estado: "+lista[j][7])
                elif (lista[j][7]=="Fallecido") or (lista[j][9]!="\\N"):
                    lciudadest[i].append(". Notificado el "+lista[j][0]+" con código divipola: "+lista[j][1]+" en "+lista[j][2]+" | edad: "+lista[j][4]+" | sexo: "+lista[j][5]+" | estado: "+lista[j][7]+" el día "+lista[j][9])
                    lciudadestf[i].append(". Notificado el "+lista[j][0]+" con código divipola: "+lista[j][1]+" en "+lista[j][2]+" | edad: "+lista[j][4]+" | sexo: "+lista[j][5]+" | estado: "+lista[j][7]+" el día "+lista[j][9])
                elif lista[j][7]=="Recuperado":
                    lciudadest[i].append(". Notificado el "+lista[j][0]+" con código divipola: "+lista[j][1]+" en "+lista[j][2]+" | edad: "+lista[j][4]+" | sexo: "+lista[j][5]+" | estado: "+lista[j][7]+" el día "+lista[j][8])
    parmenia=(100/(len(lcasos)))*(len(lc1))
    salida=""
    while salida!="salir":
        print("\nA continuación se presentan diferentes opciones que permiten explorar los casos de COVID-19 en el departamento del Quindío notificados en mayo de 2021")
        print("\n1. Número total de casos")
        print("2. Número total de casos activos")
        print("3. Número total de fallecidos")
        print("4. Número total de casos por sexo")
        print("5. Número total de casos por quinquenio")
        print("6. Número total de fallecidos por quinquenio")
        print("7. Número de casos de cada municipio")
        print("8. Número de fallecidos de cada municipio")
        print("9. Promedio de edad de los fallecidos")
        print("10. Porcentaje de casos que corresponden a la ciudad de Armenia (código 63001)")
        ingreso=0
        while ingreso<1 or 10<ingreso:
            try:
                ingreso=int(input("\nPor favor ingrese el número que corresponde a la opción de su intéres (y a continuación oprima la tecla 'enter'): "))
            except ValueError as err:
                print("\nIngreso no valido, digite un número que aparezca en la lista")
            else:
                if 0<ingreso<11:
                    True
                else:
                    print("\nIngreso no valido, digite un número que aparezca en la lista")
        if ingreso==1:            
            print("\nNúmero total de casos: "+ str(len(lcasos))) 
            ingre=pregunta()
            if ingre==True:
                for i in range (len(lcasos)):
                    print (lcasos[i])
        elif ingreso==2:
            print ("\nNúmero total de casos activos: "+str(len(lactivos)))
            ingre=pregunta()
            if ingre==True:
                for i in range (len(lactivos)):
                    print (str(i+1)+lactivos[i])
        elif ingreso==3:
            print ("\nNúmero total de fallecidos: "+str(len(lfallecidos)))
            ingre=pregunta()
            if ingre==True:
                for i in range (len(lfallecidos)):
                    print (str(i+1)+lfallecidos[i])
        elif ingreso==4:
            print ("\n1. Número total de casos por sexo masculino: "+str(len(lmasculino)))
            print ("2. Número total de casos por sexo femenino: "+str(len(lfemenino)))
            ingre=pregunta()
            if ingre==True:
                cuallista=0
                while cuallista<1 or 2<cuallista:
                    try:
                        cuallista=int(input("\nDigite el número de la lista que desea visualizar: "))
                        print("\n")
                    except ValueError as err:
                        print("\nIngreso no valido, digite un número (1 o 2)")
                    else:
                        if 0<cuallista<3:
                            True
                        else:
                            print("\nIngreso no valido, digite un número (1 o 2)")
                if cuallista==1:
                    for i in range (len(lmasculino)):
                        print (str(i+1)+lmasculino[i])
                elif cuallista==2:
                    for i in range (len(lfemenino)):
                        print (str(i+1)+lfemenino[i])
        elif ingreso==5:
            print ("\n1. Número total de casos quinquenio 0-4 años: "+str(len(lq1)))
            print ("2. Número total de casos quinquenio 5-9 años: "+str(len(lq2)))
            print ("3. Número total de casos quinquenio 10-14 años: "+str(len(lq3)))
            print ("4. Número total de casos quinquenio 15-19 años: "+str(len(lq4)))
            print ("5. Número total de casos quinquenio 20-24 años: "+str(len(lq5)))
            print ("6. Número total de casos quinquenio 25-29 años: "+str(len(lq6)))
            print ("7. Número total de casos quinquenio 30-34 años: "+str(len(lq7)))
            print ("8. Número total de casos quinquenio 35-39 años: "+str(len(lq8)))
            print ("9. Número total de casos quinquenio 40-44 años: "+str(len(lq9)))
            print ("10. Número total de casos quinquenio 45-49 años: "+str(len(lq10)))
            print ("11. Número total de casos quinquenio 50-54 años: "+str(len(lq11)))
            print ("12. Número total de casos quinquenio 55-59 años: "+str(len(lq12)))
            print ("13. Número total de casos quinquenio 60-64 años: "+str(len(lq13)))
            print ("14. Número total de casos quinquenio 65-69 años: "+str(len(lq14)))
            print ("15. Número total de casos quinquenio 70-74 años: "+str(len(lq15)))
            print ("16. Número total de casos quinquenio 75-79 años: "+str(len(lq16)))
            print ("17. Número total de casos de 80 años en adelante: "+str(len(lq17)))
            ingre=pregunta()
            if ingre==True:
                cuallista=0
                while cuallista<1 or 17<cuallista:
                    try:
                        cuallista=int(input("\nDigite el número de la lista que desea visualizar: "))
                        print("\n")
                    except ValueError as err:
                        print("\nIngreso no valido, digite un número entre 1 y 17")
                    else:
                        if 0<cuallista<18:
                            True
                        else:
                            print("\nIngreso no valido, digite un número entre 1 y 17")
                if cuallista==1:
                    for i in range (len(lq1)):
                        print (str(i+1)+lq1[i])
                elif cuallista==2:
                    for i in range (len(lq2)):
                        print (str(i+1)+lq2[i])
                elif cuallista==3:
                    for i in range (len(lq3)):
                        print (str(i+1)+lq3[i])
                elif cuallista==4:
                    for i in range (len(lq4)):
                        print (str(i+1)+lq4[i])
                elif cuallista==5:
                    for i in range (len(lq5)):
                        print (str(i+1)+lq5[i])
                elif cuallista==6:
                    for i in range (len(lq6)):
                        print (str(i+1)+lq6[i])
                elif cuallista==7:
                    for i in range (len(lq7)):
                        print (str(i+1)+lq7[i])
                elif cuallista==8:
                    for i in range (len(lq8)):
                        print (str(i+1)+lq8[i])
                elif cuallista==9:
                    for i in range (len(lq9)):
                        print (str(i+1)+lq9[i])
                elif cuallista==10:
                    for i in range (len(lq10)):
                        print (str(i+1)+lq10[i])
                elif cuallista==11:
                    for i in range (len(lq11)):
                        print (str(i+1)+lq11[i])
                elif cuallista==12:
                    for i in range (len(lq12)):
                        print (str(i+1)+lq12[i])
                elif cuallista==13:
                    for i in range (len(lq13)):
                        print (str(i+1)+lq13[i])
                elif cuallista==14:
                    for i in range (len(lq14)):
                        print (str(i+1)+lq14[i])
                elif cuallista==15:
                    for i in range (len(lq15)):
                        print (str(i+1)+lq15[i])
                elif cuallista==16:
                    for i in range (len(lq16)):
                        print (str(i+1)+lq16[i])
                elif cuallista==17:
                    for i in range (len(lq17)):
                        print (str(i+1)+lq17[i])
        elif ingreso==6:
            print ("\n1. Número total de casos de fallecidos quinquenio 0-4 años: "+str(len(lqf1)))
            print ("2. Número total de casos de fallecidos quinquenio 5-9 años: "+str(len(lqf2)))
            print ("3. Número total de casos de fallecidos quinquenio 10-14 años: "+str(len(lqf3)))
            print ("4. Número total de casos de fallecidos quinquenio 15-19 años: "+str(len(lqf4)))
            print ("5. Número total de casos de fallecidos quinquenio 20-24 años: "+str(len(lqf5)))
            print ("6. Número total de casos de fallecidos quinquenio 25-29 años: "+str(len(lqf6)))
            print ("7. Número total de casos de fallecidos quinquenio 30-34 años: "+str(len(lqf7)))
            print ("8. Número total de casos de fallecidos quinquenio 35-39 años: "+str(len(lqf8)))
            print ("9. Número total de casos de fallecidos quinquenio 40-44 años: "+str(len(lqf9)))
            print ("10. Número total de casos de fallecidos quinquenio 45-49 años: "+str(len(lqf10)))
            print ("11. Número total de casos de fallecidos quinquenio 50-54 años: "+str(len(lqf11)))
            print ("12. Número total de casos de fallecidos quinquenio 55-59 años: "+str(len(lqf12)))
            print ("13. Número total de casos de fallecidos quinquenio 60-64 años: "+str(len(lqf13)))
            print ("14. Número total de casos de fallecidos quinquenio 65-69 años: "+str(len(lqf14)))
            print ("15. Número total de casos de fallecidos quinquenio 70-74 años: "+str(len(lqf15)))
            print ("16. Número total de casos de fallecidos quinquenio 75-79 años: "+str(len(lqf16)))
            print ("c17. Número total de casos de fallecidos de 80 años en adelante: "+str(len(lqf17)))
            ingre=pregunta()
            if ingre==True:
                cuallista=0
                while cuallista<1 or 17<cuallista:
                    try:
                        cuallista=int(input("\nDigite el número de la lista que desea visualizar: "))
                        print("\n")
                    except ValueError as err:
                        print("\nIngreso no valido, digite un número entre 1 y 17")
                    else:
                        if 0<cuallista<18:
                            True
                        else:
                            print("\nIngreso no valido, digite un número entre 1 y 17")
                if cuallista==1:
                    for i in range (len(lqf1)):
                        print (str(i+1)+lqf1[i])
                elif cuallista==2:
                    for i in range (len(lqf2)):
                        print (str(i+1)+lqf2[i])
                elif cuallista==3:
                    for i in range (len(lqf3)):
                        print (str(i+1)+lqf3[i])
                elif cuallista==4:
                    for i in range (len(lqf4)):
                        print (str(i+1)+lqf4[i])
                elif cuallista==5:
                    for i in range (len(lqf5)):
                        print (str(i+1)+lqf5[i])
                elif cuallista==6:
                    for i in range (len(lqf6)):
                        print (str(i+1)+lqf6[i])
                elif cuallista==7:
                    for i in range (len(lqf7)):
                        print (str(i+1)+lqf7[i])
                elif cuallista==8:
                    for i in range (len(lqf8)):
                        print (str(i+1)+lqf8[i])
                elif cuallista==9:
                    for i in range (len(lqf9)):
                        print (str(i+1)+lqf9[i])
                elif cuallista==10:
                    for i in range (len(lqf10)):
                        print (str(i+1)+lqf10[i])
                elif cuallista==11:
                    for i in range (len(lqf11)):
                        print (str(i+1)+lqf11[i])
                elif cuallista==12:
                    for i in range (len(lqf12)):
                        print (str(i+1)+lqf12[i])
                elif cuallista==13:
                    for i in range (len(lqf13)):
                        print (str(i+1)+lqf13[i])
                elif cuallista==14:
                    for i in range (len(lqf14)):
                        print (str(i+1)+lqf14[i])
                elif cuallista==15:
                    for i in range (len(lqf15)):
                        print (str(i+1)+lqf15[i])
                elif cuallista==16:
                    for i in range (len(lqf16)):
                        print (str(i+1)+lqf16[i])
                elif cuallista==17:
                    for i in range (len(lqf17)):
                        print (str(i+1)+lqf17[i])
        elif ingreso==7:
            print ("\n1. Número de casos de "+str(lcselect[0])+":   "+str(len(lc1)))
            print ("2. Número de casos de "+str(lcselect[1])+":   "+str(len(lc2)))
            print ("3. Número de casos de "+str(lcselect[2])+":  "+str(len(lc3)))
            print ("4. Número de casos de "+str(lcselect[3])+":   "+str(len(lc4)))
            print ("5. Número de casos de "+str(lcselect[4])+":   "+str(len(lc5)))
            print ("6. Número de casos de "+str(lcselect[5])+":   "+str(len(lc6)))
            print ("7. Número de casos de "+str(lcselect[6])+":   "+str(len(lc7)))
            print ("8. Número de casos de "+str(lcselect[7])+":   "+str(len(lc8)))
            print ("9. Número de casos de "+str(lcselect[8])+":   "+str(len(lc9)))
            print ("10. Número de casos de "+str(lcselect[9])+":   "+str(len(lc10)))
            print ("11. Número de casos de "+str(lcselect[10])+":   "+str(len(lc11)))
            print ("12. Número de casos de "+str(lcselect[11])+":   "+str(len(lc12)))
            ingre=pregunta()
            if ingre==True:
                cuallista=0
                while cuallista<1 or 12<cuallista:
                    try:
                        cuallista=int(input("\nDigite el número de la lista que desea visualizar: "))
                        print("\n")
                    except ValueError as err:
                        print("\nIngreso no valido, digite un número entre 1 y 12")
                    else:
                        if 0<cuallista<13:
                            True
                        else:
                            print("\nIngreso no valido, digite un número entre 1 y 12")
                if cuallista==1:
                    for i in range (len(lc1)):
                        print (str(i+1)+lc1[i])
                elif cuallista==2:
                    for i in range (len(lc2)):
                        print (str(i+1)+lc2[i])
                elif cuallista==3:
                    for i in range (len(lc3)):
                        print (str(i+1)+lc3[i])
                elif cuallista==4:
                    for i in range (len(lc4)):
                        print (str(i+1)+lc4[i])
                elif cuallista==5:
                    for i in range (len(lc5)):
                        print (str(i+1)+lc5[i])
                elif cuallista==6:
                    for i in range (len(lc6)):
                        print (str(i+1)+lc6[i])
                elif cuallista==7:
                    for i in range (len(lc7)):
                        print (str(i+1)+lc7[i])
                elif cuallista==8:
                    for i in range (len(lc8)):
                        print (str(i+1)+lc8[i])
                elif cuallista==9:
                    for i in range (len(lc9)):
                        print (str(i+1)+lc9[i])
                elif cuallista==10:
                    for i in range (len(lc10)):
                        print (str(i+1)+lc10[i])
                elif cuallista==11:
                    for i in range (len(lc11)):
                        print (str(i+1)+lc11[i])
                elif cuallista==12:
                    for i in range (len(lc12)):
                        print (str(i+1)+lc12[i])
        elif ingreso==8:
            print ("\n1. Número de fallecidos de "+str(lcselect[0])+":   "+str(len(lcf1)))
            print ("2. Número de fallecidos de "+str(lcselect[1])+":   "+str(len(lcf2)))
            print ("3. Número de fallecidos de "+str(lcselect[2])+":   "+str(len(lcf3)))
            print ("4. Número de fallecidos de "+str(lcselect[3])+":   "+str(len(lcf4)))
            print ("5. Número de fallecidos de "+str(lcselect[4])+":   "+str(len(lcf5)))
            print ("6. Número de fallecidos de "+str(lcselect[5])+":   "+str(len(lcf6)))
            print ("7. Número de fallecidos de "+str(lcselect[6])+":   "+str(len(lcf7)))
            print ("8. Número de fallecidos de "+str(lcselect[7])+":   "+str(len(lcf8)))
            print ("9. Número de fallecidos de "+str(lcselect[8])+":   "+str(len(lcf9)))
            print ("10. Número de fallecidos de "+str(lcselect[9])+":   "+str(len(lcf10)))
            print ("11. Número de fallecidos de "+str(lcselect[10])+":   "+str(len(lcf11)))
            print ("12. Número de fallecidos de "+str(lcselect[11])+":   "+str(len(lcf12)))
            ingre=pregunta()
            if ingre==True:
                cuallista=0
                while cuallista<1 or 12<cuallista:
                    try:
                        cuallista=int(input("\nDigite el número de la lista que desea visualizar: "))
                        print("\n")
                    except ValueError as err:
                        print("\nIngreso no valido, digite un número entre 1 y 12")
                    else:
                        if 0<cuallista<13:
                            True
                        else:
                            print("\nIngreso no valido, digite un número entre 1 y 12")
                if cuallista==1:
                    for i in range (len(lcf1)):
                        print (str(i+1)+lcf1[i])
                elif cuallista==2:
                    for i in range (len(lcf2)):
                        print (str(i+1)+lcf2[i])
                elif cuallista==3:
                    for i in range (len(lcf3)):
                        print (str(i+1)+lcf3[i])
                elif cuallista==4:
                    for i in range (len(lcf4)):
                        print (str(i+1)+lcf4[i])
                elif cuallista==5:
                    for i in range (len(lcf5)):
                        print (str(i+1)+lcf5[i])
                elif cuallista==6:
                    for i in range (len(lcf6)):
                        print (str(i+1)+lcf6[i])
                elif cuallista==7:
                    for i in range (len(lcf7)):
                        print (str(i+1)+lcf7[i])
                elif cuallista==8:
                    for i in range (len(lcf8)):
                        print (str(i+1)+lcf8[i])
                elif cuallista==9:
                    for i in range (len(lcf9)):
                        print (str(i+1)+lcf9[i])
                elif cuallista==10:
                    for i in range (len(lcf10)):
                        print (str(i+1)+lcf10[i])
                elif cuallista==11:
                    for i in range (len(lcf11)):
                        print (str(i+1)+lcf11[i])
                elif cuallista==12:
                    for i in range (len(lcf12)):
                        print (str(i+1)+lcf12[i])
        elif ingreso==9:
            print("\nPromedio de edad de los fallecidos: "+str(promedioef) +" años")
        elif ingreso==10:
            print("\nPorcentaje de casos que corresponden a la ciudad de Armenia: "+str(parmenia) +"%")
        salida=""
        while True:
            if salida=="S" or salida=="s" or salida=="si" or salida=="SI":
                break
            elif salida=="N" or salida=="n" or salida=="no" or salida=="NO":
                print("\nEl programa finaliza ahora\n")
                salida="salir"
                break
            else:
                salida=input("\n¿Desea realizar otra consulta? (S/N): ")