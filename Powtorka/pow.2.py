def sum_of_values(dict):
    suma = 0
    for i in dict.values():
        suma += i
    return suma
dict1 = {'data1':10, 'data2':-4, 'data3':2}
print(sum_of_values(dict1))