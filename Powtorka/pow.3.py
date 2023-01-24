#w numpy mozna podsniesc poprzez tab1**tab2 jesli listy sa tej samej dlugosci

def potega(lista_1,lista_2):
    wynik = []
    if len(lista_1) != len(lista_2):
        return wynik
    for x in range(len(lista_1)):
        wynik.append(lista_1[x]**lista_2[x])
    return wynik

print(potega([2,2,2], [2,3,4]))