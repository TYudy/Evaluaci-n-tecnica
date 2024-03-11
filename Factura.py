def Factura():

    Cliente = input("Por favor ingrese el nombre del cliente: ")
    Monto = float(input("Por favor ingrese el monto: "))
    Total = float
    Desc = 0.0
    
    

    if Monto >= 200000:
         Desc = (Monto * 0.15)
         Porc = "15%"
    elif Monto >= 50000:
         Desc =(Monto * 0.2)
         Porc = "2%"
         
    elif Monto >= 20000:
         Desc =(Monto *0.015)
         Porc = "1.5%"
    else:
         Desc = 0
         Porc ="No aplica"



    Total = Monto - Desc



    print("{:<35}{:^5}{:<30}".format(" ","FACTURA",""))
    print("_"*85)
    print("_"*85)
    print(" "*80)
    print ("{:5}{:<20} {:<20}".format(" ","Monto sin descuento",Monto))
    print("-"*80)
    print("{:^5}{:<20}{:<20}{:<20}{:^5}".format(" ","Total con descuento: ",Total,"Descuento:",Porc))
    print("_"*85)
    print("_"*85)
    print(f"Muchas gracias {Cliente} por su compra, vuelva pronto")
    print("_"*85)
    

Factura()