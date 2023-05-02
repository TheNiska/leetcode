from timeit import timeit
from random import randint
#arr = [randint(0, 100000) for x in range(100000)]

def find_simple(arr):
    target = randint(0, 10000)
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

def bin_search(arr):
    target = randint(0, 10000)
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] > target:
            right = mid - 1
        elif arr[mid] < target:
            left = mid + 1
        else:
            return mid
    return -1




#t1 = timeit('find_simple(arr)', setup='from __main__ import find_simple, arr', number=1000)
#t2 = timeit('bin_search(arr)', setup='from __main__ import bin_search, arr', number=1000)
#print(t1)
#print(t2)

print(globals())



