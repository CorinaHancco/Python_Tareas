class Proceso:
    def __init__(self, palabra):
        self.palabra = palabra
    def metodo(self):
        cont = 0
        for letra in self.palabra:
            if letra == "#" and cont != 0:
                letra_anterior=self.palabra[cont-1]
                nueva_cadena=self.palabra.replace(f"{letra_anterior}{letra}","")
                self.palabra=nueva_cadena
            elif letra == "#" and cont == 0:
                letra_anterior=self.palabra[cont]
                nueva_cadena=self.palabra.replace(f"{letra_anterior}{letra}","")
                self.palabra=nueva_cadena
            cont +=1
        print(self.palabra)

cadena=input("Ingrese la cadena : ")
objeto_tipo_Proceso=Proceso(cadena)
objeto_tipo_Proceso.metodo()

