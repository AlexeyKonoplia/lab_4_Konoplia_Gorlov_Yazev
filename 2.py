import timeit
from sorts import bsort
from sorts import psort
import random

arr1 = [random.randint(-1000,1000) for i in range(10)]
arr2 = [random.randint(-1000,1000) for i in range(100)]
arr3 = [random.randint(-1000,1000) for i in range(1000)]
arr1_1 = arr1.copy()
arr2_1 = arr2.copy()
arr3_1 = arr3.copy()
print('Блочная сортировка для 10, 100, 1000 элементов')

start_time = timeit.default_timer()
b1 = bsort(arr1)
print(timeit.default_timer() - start_time)

start_time = timeit.default_timer()
b2 = bsort(arr2)
print(timeit.default_timer() - start_time)

start_time = timeit.default_timer()
b3 = bsort(arr3)
print(timeit.default_timer() - start_time)

print('Пирамидальная соритровка для 10, 100, 1000 элементов')

start_time = timeit.default_timer()
p1 = psort(arr1_1)
print(timeit.default_timer() - start_time)

start_time = timeit.default_timer()
p2 = psort(arr2_1)
print(timeit.default_timer() - start_time)

start_time = timeit.default_timer()
p3 = psort(arr3_1)
print(timeit.default_timer() - start_time)

