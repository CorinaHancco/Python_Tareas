numero = int(input("Ingrese un numero: "))
for i in range(1,numero,2):
    if i % 2 == 0:
        break
    else:
        print(i)