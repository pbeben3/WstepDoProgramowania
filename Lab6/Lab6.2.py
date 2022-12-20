sample_dict = {
"name": "Kelly",
"surname": "Jones",
"age": 25,
"salary": 8000,
"city": "New york"}

"""""
for k in sample_dict.keys():
 print(k,sampled_dict[k])
"""
for k,v in sample_dict.items():
 print(f'{k:<10}={v:>10}') #formatowanie wyswietlanego tekstu(znak pokazuje strone do ktorej wyrownujemy tekst)
new_dict = {}
lista = ["age","city"]
for i in range(0,len(lista)):
 if lista[i] in sample_dict:
  new_dict[lista[i]] = sample_dict[lista[i]]
print(new_dict)
for l in lista:
 if l in sample_dict:
  del sample_dict[l]
for k,v in sample_dict.items():
 print(f'{k:<10}={v:>10}')
#za pomoca funckji pop mozna zwrocic klucz i np komunikat brak wartosci
if "Jones" in sample_dict.values():
 print("Jones znajduje sie w slowniku")
else:
 print("Jones nie znajduje sie w slowniku")

