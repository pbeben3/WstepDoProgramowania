import numpy as np
potegi = []

'''
for x in range(7, -1, -1):
    potegi.append(2**x)
print(potegi)
'''

potegi = [2**x for x in range(7,-1,-1)] #lista skladana
print(potegi)
wagi = np.array(potegi)
print(wagi)
liczba_bin = np.random.randint(0,2,8)
print(liczba_bin)
print('--------------------------')
wynik = liczba_bin*wagi
print(wynik)
print('-------------------------')
print(wynik.sum())

#konwersja z zapisu binarnego na dziesietny