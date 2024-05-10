import numpy as np
lista = [[2,100], [23, 3]]
lista2 = [[2,100], [23, 3]]
print(lista)
a = np.array(lista)
print(a)
print(np.random.random((3,3,4)))

print(np.array(lista2)==2)
print(a.reshape((2,2)))
print(a.size)
print(a.shape)
b = np.expand_dims(a, axis= 1)
print(b)
print(b.shape)
print(a.argmax)