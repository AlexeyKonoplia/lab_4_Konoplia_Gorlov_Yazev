import timeit
from sorts import *
import random



arr1 = [random.randint(-1000,1000) for i in range(10)]
arr2 = [random.randint(-1000,1000) for i in range(100)]
arr3 = [random.randint(-1000,1000) for i in range(1000)]
print('Быстрая сортировка для 10, 100, 1000 элементов')

start_time = timeit.default_timer()
q1 = qsort(arr1)
print(timeit.default_timer() - start_time)

start_time = timeit.default_timer()
q2 = qsort(arr2)
print(timeit.default_timer() - start_time)

start_time = timeit.default_timer()
q3 = qsort(arr3)
print(timeit.default_timer() - start_time)


print('Сортировка расческой для 10, 100, 1000 элеметов')

start_time = timeit.default_timer()
r1 = rsort(arr1)
print(timeit.default_timer() - start_time)

start_time = timeit.default_timer()
r2 = rsort(arr2)
print(timeit.default_timer() - start_time)

start_time = timeit.default_timer()
r3 = rsort(arr3)
print(timeit.default_timer() - start_time)