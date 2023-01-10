def intersection(lista1,lista2):
    lista3 = []
    for i in lista1:
        if i in lista2:
            lista3.append(i)
    return lista3
l1 = [6,3,5,1,2,88,0,51]
l2 = [55,11,22,2,88,100]
print(intersection(l1,l2))
wynik = intersection('przemek','przemysl')
print(wynik)