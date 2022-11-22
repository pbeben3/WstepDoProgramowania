#lista = [random.randint(1,10) for i in range(x)] alternatywny sposob losowej listy
from random import randint
e = int(input("Podaj liczbe elementow zestawu 1: "))
zestaw_1=[]
for i in range(0,e):
    zestaw_1.append(randint(0, 10))
print(zestaw_1)
print()
l= int(input("Podaj liczbe elementow zestawu 2: "))
zestaw_2=[]
for i in range(0,l):
    zestaw_2.append(randint(5, 15))
print(zestaw_2)
print()
p = int(input("Podaj liczbe ktorej chcesz poszukac: "))
if p in zestaw_1 and p in zestaw_2:
    print("Liczba znajduje sie w obu zestawach")
elif p in zestaw_1:
    print("Liczba z zestawu 1")
elif p in zestaw_2:
    print("Liczba z zestawu 2")
else:
    print("Nie ma takiej liczby w obu zestawach")
print()
zestaw1_2 = zestaw_1 + zestaw_2
zestaw1_2.sort()
print(f"suma obydwu zestawow {zestaw1_2}")

#L2=sorted(L) zwracanie posortowanych elementow listy L do nowej listy L2