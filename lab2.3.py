print("Jaką operację chcesz wykonać? "
       "\n1)dodawanie"
       "\n2)odejmowanie"
       "\n3)mnożenie"
       "\n4)dzielenie"
       "\n5)potegowanie")
op = int(input("Podaj numer operacji: "))

a = int(input("Podaj argument 1:"))
b = int(input("Podaj argument 2:"))
if op == 1:
      w = a + b
elif op == 2:
      w = a - b
elif op == 3:
      w = a * b
elif op == 4:
     if b != 0:
        w = a / b
     else:
         print("bład-nie dzielimy przez 0")
         quit()
elif op == 5:
      w = a ** b
print(f"wynik: {w}")