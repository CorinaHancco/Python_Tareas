diccionario =[{'a':1},{'a':2}]
propiedad = 'a'
def secuencia(d,p):
    valores=[]
    for i in d:
        varible = i
        if varible.keys() == p:
            valores.append(varible.items())
            print(varible)
    return valores

print(secuencia(diccionario,propiedad))