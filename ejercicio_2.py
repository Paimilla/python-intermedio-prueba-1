def main():
    Renta_anual = float(input("¿cual es su renta anual?: "))
    if Renta_anual < 10000:
        pago = 5
    elif Renta_anual < 20000:
        pago = 15
    elif Renta_anual < 35000:
        pago = 20
    elif Renta_anual < 60000:
        pago = 30
    else:
        pago = 45
    impuesto_total = Renta_anual * pago / 100 
    print("usted debe pagar = " + str(impuesto_total)+"€")

if __name__ == '__main__':
    main()