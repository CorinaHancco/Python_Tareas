numero_limite = int(input("Ingrese el maximo numero: "))
def multiplo_de_tres(numero):
    contador = 0
    for i in range(1,numero+1):
        if i % 3 == 0:
            print(i)
            contador +=1
    print(f"hay un total de {contador} numeros multiplos de tres")
multiplo_de_tres(numero_limite)