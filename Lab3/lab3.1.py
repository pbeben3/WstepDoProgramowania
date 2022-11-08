l1 = int(input("Podaj liczbe 1: "))
l2 = int(input("Podaj liczbe 2: "))
if l1>l2:
    l1,l2=l2,l1
while l1 <= l2:
    print(l1)
    l1=l1+1