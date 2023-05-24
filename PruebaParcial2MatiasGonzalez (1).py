subtotal=0
tratCar=0
tratOrt=0
dental=0
opc=0
opc2=0
trab=0
flag=False
while flag==False:
      print("1)Cotizacion \n2)Reiniciar Cotizacion \n3)Salir")
      try:
          opc=int(input("Ingrese la opcion que desea: "))
          if 0<opc<=3:
            flag=True
          else:
            print("Opcion debe ser 1,2 o 3")
      except:    
          print("Opcion Invalida")
if opc==2:
    subtotal=0
    tratCar=0
    tratOrt=0
    dental=0
    opc=0
    opc2=0
    trab=0
    flag=False
elif opc==1:
    while opc2!=4:
      print("EL DIENTE DE ORO")
      print("-"*50)
      print("1)Carillas Porcelana: $250000 \n2)Implantes Dentales:$475000 \n3)Ortodoncia Brackets:$800000 \n4)Terminar Cotizacion")  
      while True:
        try:
          opc2=int(input("Ingrese la opcion que desea: "))
          if 0<opc2<=4:
              break
          else:
            print("Opcion invalida")   
        except:
          print("Opcion debe ser un numero")
      if opc2==1:
        subtotal=subtotal+250000
        tratCar=tratCar+1
      elif opc2==2:
        subtotal=subtotal+475000
        dental=dental+1
      elif opc2==3:
        subtotal=subtotal+800000
        tratOrt=tratOrt+1
      else:
        print("¿Que tipo de trabajador es usted?")
        while True:
          try:
              trab=int(input("1)Trabajador Auxiliar \n2)Trabajador Administrativo \n3)Trabajador docente \nIngrese Opcion:"))
              if 0<trab<=3:
                break
              else:
                print("Opcion Invalida")
          except:
              print("La opcion debe ser un numero")
        if trab==1:
          print("-"*50)
          print("\t\tCotizacion ")
          print("-"*50)
          print(f"Carillas porcelana ({tratCar}) \nImplantes dentales({dental})\nOrtodoncia Brackets({tratOrt}))")
          desct=subtotal*0.15
          total=subtotal-desct
          cuota=total/12
          print(f"El valor de su cotizacion es {total}")
          print(f"Su descuento es de",round(desct))
          print(f"Total:{total}")
          print("el total se paga en 12 cuotas de: ",round(cuota))
          flag=False
        elif trab==2:
          print("-"*50)
          print("\t\tCotizacion ")
          print("-"*50)
          print(f"Carillas porcelana ({tratCar}) \nImplantes dentales({dental})\nOrtodoncia Brackets({tratOrt}))")
          desct=subtotal*0.10
          total=subtotal-desct
      
          cuota=total/12
          print(f"El valor de su cotizacion es {subtotal}")
          print(f"Su descuento es de:",round(desct))
          print(f"Total:{total}")
          print("el total se paga en 12 cuotas de ",round(cuota))
        else:
          print("-"*50)
          print("\t\tCotizacion ")
          print("-"*50)
          print(f"Carillas porcelana ({tratCar}) \nImplantes dentales({dental})\nOrtodoncia Brackets({tratOrt}))")
          desct=subtotal*0.05
          total=subtotal-desct
          cuota=total/12
          print(f"El valor de su cotizacion es {subtotal}")
          print(f"Su descuento es de:",round(desct))
          print(f"Total:{total}")
          print(f"el total se paga en 12 cuotas de ",round(cuota))        
else:
  print("Adios :D")
   
