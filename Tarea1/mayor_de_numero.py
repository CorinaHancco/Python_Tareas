number_1=float(input("Ingrese un primer numero: "))
number_2=float(input("Ingrese un segundo numero: "))
if number_1 > number_2:
    print(f"El numero mayor es: {number_1}")
elif number_2 > number_1:
    print(f"El numero mayor es: {number_2}")
else:
    print("Los numeros son iguales, debe ingresar dos valores diferentes")