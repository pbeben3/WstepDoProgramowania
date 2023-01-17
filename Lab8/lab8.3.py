import numpy as np
tablica = np.zeros((3,3))
print(tablica)
print('-----------------')
#tablica[1: , :2] = 1
tablica[: , 2:] = 1
print(tablica)
#tablica[:3 , [0,2]] = 1 robienie wycinka w dwoch miejscach
'''
na 4 albo 5 porownywanie tablic

'''