'''uzytkownik podaje n liczb program liczy ile jest liczb wiekszych od 0 '''
lista = []
n = int(input('podaj n: '))
for i in range(0,n):
    lista.append(int(input('podaj element: ')))
w = 0
for k in lista:
    if k!=0:
        w += 1
print(f'jest {w} liczb wiekszych od 0')



#rozw z zajec
'''
n = int(input())
p = 0
for i in range(0,n):
    a = float(input(f"Enter numbers like a float{i + 1}: "))
    if a != 0:
       p = p + 1;
print(p)
'''
#1.1 W oparciu o program z zadania 1, napisz funkcję, do której przekazujemy liczbę n. Funkcja pobierze od
#użytkownika n liczb i zwróci, sumę tych liczb.