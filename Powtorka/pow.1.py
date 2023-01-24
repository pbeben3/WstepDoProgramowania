def find(lista,szukana):
    wyniki =[]
    for i in range(len(lista)):
        if lista[i] == szukana:
            wyniki.append(i)
    return wyniki
lista = [4,6,2,3,0,5,1,7]
szukana = int(input('podaj szukana liczbe: '))
print(find(lista,szukana))

