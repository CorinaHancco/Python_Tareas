def numeros_impares():
    cont = 0
    for i in range(101):
        if i % 2 != 0:
            print(i)
            cont +=1
    print(f"Total de numeros impares: {cont}")
numeros_impares()