
import random
"""
Punkty = []
for x in range(15):
    Punkty.append(round(random.uniform(0, 50), 2))
"""
Punkty = [round(random.uniform(0, 50), 2) for x in range(15)]
print(Punkty)
Min = min(Punkty)
Max = max(Punkty)
print(f"Min: {Min}")
print(f"Max: {Max}")
Sprawdzana_Wartosc = float(input("Podaj wartość do sprawdznenia: "))
if Sprawdzana_Wartosc in Punkty:
    print(f"Wartość {Sprawdzana_Wartosc} ma index {Punkty.index(Sprawdzana_Wartosc)}")
else:
    print(f"Wartość {Sprawdzana_Wartosc} nie występuje w liscie")

suma = sum(Punkty)
ilosc = len(Punkty)
srednia = suma/ilosc
print(f"srednia punktow wynosi {round(srednia,2)}")

mn = []
we = []
for x in Punkty:
    if x<srednia:
        mn.append(x)
    else:
        we.append(x)
"""
alternatywnie lista skladana
mn = [x for x in Punkty if x<srednia]
we = [x for x in Punkty if x>srednia]
"""
print(mn, len(mn))
print(we, len(we))
