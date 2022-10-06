def main():
    materias = ["matematicas" , "fisica", "quimica", "historia", "lengua"]
    reprobados = []
    for i in range(5):
        notas = int(input("ingrese su nota de la asignatura  " + str(materias[i]) + ": "))
        if notas < 40:
            reprobados.append(materias[i])

    print("Tienes que repetir " + str(reprobados) + " :(")

if __name__ == '__main__':
    main()