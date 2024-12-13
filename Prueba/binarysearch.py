import time as t
"""
Algoritmo de busqueda binaria en Python
"""
# funcion binarysearch
def binarysearch(array, target):
    left = 0
    right = len(array) - 1
    while left <= right:
        mid = (left + right) // 2
        if array[mid] == target:
            return mid
        elif array[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1
ar = [9,16,23,34,42,55,67,71]


start = t.time()
res = binarysearch(ar, 55)

end = t.time()
print(ar)
print(res, ar[res])
print(end - start)