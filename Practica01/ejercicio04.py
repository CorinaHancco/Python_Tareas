numero_de_mes=int(input("Ingrese el numero de mes: "))

def mensaje(trimestre):
     print(f"El numero de mes ingresado es parte del {trimestre} trimestre")

if numero_de_mes >= 1 and numero_de_mes <= 3:
    mensaje("primer")
elif numero_de_mes >= 4 and numero_de_mes <= 6:
    mensaje("segundo")
elif numero_de_mes >= 7 and numero_de_mes <= 9:
    mensaje("tercer")
elif numero_de_mes >= 10 and numero_de_mes <= 12:
    mensaje("cuarto")

