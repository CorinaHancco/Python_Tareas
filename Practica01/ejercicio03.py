grados_centigrados=float(input("Ingrese la temperatura en grados centigrados: "))
def conversor(grados):
    grados_fahrenheit = int((grados*9/5)+32)
    print(f"La temperatura en grados fahrenheit es: {grados_fahrenheit}")

conversor(grados_centigrados)