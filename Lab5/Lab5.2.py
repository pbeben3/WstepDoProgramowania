x = list(range(1,11))
print(x)
print(x[-3:])
x[:0]=x[-3:]
x[-3:]=[]
print(x)
y=x[:]
# zamiana wycinkiem kopia adresow zmiany w jednej nie maja wplywu na druga dziala na obiektach niemutowalnych liczby stringi
# w listach y=x kopiuje indeks obiektu(jak zmieniamy cos w y to tez w x )
y[8]=100
print(x)
print(y)
