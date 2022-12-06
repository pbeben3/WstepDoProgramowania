zwierzeta = []

for  x in range(7):
    z = input("Podaj nazwe zwierzecia:" )
    zwierzeta.append(z)
print(zwierzeta)
zwierzeta.sort()
print(zwierzeta[0],zwierzeta[-3:],len(zwierzeta))