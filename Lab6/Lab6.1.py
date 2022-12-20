values = [10,20,30]
keys = ['ten','twenty','thirty']
dict_1 = dict(zip(keys,values))
print(dict_1)
dict_2 =(dict(thirty=30, fourty=40,fifty=50))
print(dict_2)
dict_1.update(dict_2)
print(dict_1)
dict_3 = {}
#tworzenie nowego slownika z wartosciami dict1 i dict 2
dicnt_3.update(dict_1)
dict_3.update(dict_2)

""""
#2 sposob na tworzenie slownika za pomoca petli for
D = {}
for i in range(0,len(values)):
    D[keys[i]] =  values[i]
print(D)
"""
""""
#slownik skladany
D = {keys[i]:values[i] for i in range(len(keys))}
print(D)
"""