
def iva(factura, porcentaje_iva):  
    if(porcentaje_iva == ""):
           porcentaje_iva = 19       
    porcentaje_iva = int(porcentaje_iva)
    return factura + factura*porcentaje_iva/100
    
def main():
    factura = int(input("Ingrese la cantidad sin iva: "))
    porcentaje_iva = (input("ingrese porcetaje de iva a aplicar = ")) 
    print(iva(factura,porcentaje_iva))

if __name__ == '__main__':
    main()