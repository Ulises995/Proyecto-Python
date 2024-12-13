import time as t
"""
El algoritmo de quicksort es un algoritmo de ordenamiento
basado en el quicksort. El quicksort consiste en tomar un elemento
"""

# funcion quicksort
def quicksort(array):
    if len(array) < 2:
        return array
    else:
        pivot = array[0]
        less = [i for i in array[1:] if i <= pivot]
        greater = [i for i in array[1:] if i > pivot]
        return quicksort(less) + [pivot] + quicksort(greater)
    
ar= [8,6,3,4,5,7,1,9,2]

start = t.time()

res = quicksort(ar)

end = t.time()
print(ar)
print(res)

print(end - start)

import n_Aleator as ale
ar = ale.aleator_array(100, 0, 50)

start = t.time()
res = quicksort(ar)

end = t.time()
print(ar)
print(res)

print(end - start)