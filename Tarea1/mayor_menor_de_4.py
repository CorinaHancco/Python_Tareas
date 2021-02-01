numero_1=float(input("Ingrese el primer numero: "))
numero_2=float(input("Ingrese el segundo numero: "))
numero_3=float(input("Ingrese el tercer numero: "))
numero_4=float(input("Ingrese el cuarto numero: "))
mayor_numero=0
menor_numero=0
def mayor(a,b):
    if a > b:
        mayor_numero = a
    else:
        mayor_numero = b
    return mayor_numero

def menor(a,b):
    if a < b:
        menor_numero = a
    else:
        menor_numero = b
    return menor_numero

if numero_1 != numero_2 and numero_2 != numero_3 and numero_1 != numero_3:
    print(f"El mayor numero entre {numero_1}, {numero_2} , {numero_3} y {numero_4} es : {mayor(mayor(numero_1,numero_2),mayor(numero_3,numero_4))}")
    print(f"El menor numero entre {numero_1}, {numero_2} , {numero_3} y {numero_4} es : {menor(menor(numero_1,numero_2),menor(numero_3,numero_4))}")

else:
    print("ERROR, es necesario ingresar tres valores diferentes")
