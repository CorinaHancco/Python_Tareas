longitud=float(input("Ingrese la longitud del poligono: "))
ancho=float(input("Ingrese el ancho del poligono: "))
if longitud == ancho:
    area = round(longitud*ancho,2)
    print(f"El area del cuadrado es: {area}")
else:
    perimetro = round(2*longitud + 2*ancho,2)
    print(f"El perimetro del rectangulo es: {perimetro}")