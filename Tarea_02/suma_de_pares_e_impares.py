def sumas_par_impar():
    suma_pares = 0
    suma_impares = 0
    for i in range(1,101):
        print(i)
        if i % 2 == 0:
            suma_pares += i
        else:
            suma_impares += i
    print(f"La suma de numeros pares es: {suma_pares}")
    print(f"La suma de numeros impares es: {suma_impares} ")
sumas_par_impar()