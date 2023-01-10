def dodawanie(x,y):
    return x+y
def odejmowanie(x,y):
    return x-y
def mnozenie(x,y):
    return x*y
def dzielenie(x,y):
    if y==0:
        return None
    return x/y

kalk = {'+':dodawanie, '-':odejmowanie, '*':mnozenie, '/':dzielenie}
l1 = float(input('Podaj liczbe: '))
l2 = float(input('Podaj liczbe: '))
znak = input('Podaj dzialanie(+;-;*;/): ')
wynik = kalk[znak](l1,l2)
print(f'wynik {znak} to : {wynik}')