import timeit
from sorts import qsort
from sorts import rsort

arr = list(map(int, input().split()))
answer = input('Каким алгоритмом вы хотите сортировать масив? (q/c)')

if answer == 'q':
    start_time = timeit.default_timer()
    a = qsort(arr)
    print(f'Массив: {rsort(arr)}')
    print(f'Время выполнения {timeit.default_timer() - start_time}')
elif answer == 'c':
    start_time = timeit.default_timer()
    a = rsort(arr)
    print(f'Массив: {rsort(arr)}')
    print(f'Время выполнения {timeit.default_timer() - start_time}')
    