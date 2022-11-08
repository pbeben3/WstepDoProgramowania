s = int(input("Podaj liczbe studentow: "))
i = 1
sr = 0
while i <= s:
    lp = int(input(f"Podaj punkty studenta {i}: "))
        if lp < 0 or lp > 100:
            continue
        else:
            sr = sr + lp
            i = i+1
print(f"Średnia punktów studentów = {sr/s}")