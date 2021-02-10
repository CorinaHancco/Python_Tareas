lista = ["i","have","no","space"]
def funcion(listas):
    list = []
    variable=""
    for i in lista:
        variable= variable+i
        list.append(variable)
    return list
print(funcion(lista))
