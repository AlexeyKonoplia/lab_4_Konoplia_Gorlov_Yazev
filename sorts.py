#быстрая сортировка
def qsort(arr):
    if len(arr) <= 1:
        return arr
    else:
        x = arr[len(arr)//2]
    
    l_nums, r_nums, m_nums = [],[],[]
    for i in arr:
        if i < x: l_nums += [i]
        elif i > x: r_nums += [i]
        else: m_nums += [i]
    return qsort(l_nums) + m_nums + qsort(r_nums)

#Сортировка расческой
def rsort(arr):
    step = int(len(arr)/1.247)
    swap = 1
    while step > 1 or swap > 0:
        swap = 0
        i = 0
        while i + step < len(arr):
            if arr[i] > arr[i+step]:
                arr[i], arr[i+step] = arr[i+step], arr[i]
                swap += 1
            i = i + 1
        if step > 1:
            step = int(step / 1.247)
    return arr

#Блочная сортировка
def bsort(input_list):
    # Находим максимальное значение в списке. Затем используем длину списка, чтобы определить, какое значение в списке попадет в какой блок
    max_value = max(input_list)
    size = max_value/len(input_list)
    min_value = min(input_list)
    flag = 0
    if min_value < 0:
        for i in range(len(input_list)):
            input_list[i] -= min_value 
        size -= min_value
        flag = 1

    # Создаем n пустых блоков, где n равно длине входного списка
    delta = max_value - min_value  # диапазон, в котором находятся значения элементов массива
    p = round(delta / len(input_list), 2)  # диапазон значений для одного "блока"
    bucks = [[] for i in range(int(max_value / p)+1)]
    buckets_list= []
    for x in range(len(input_list)):
        buckets_list.append([]) 

    # Помещаем элементы списка в разные блоки на основе size
    for i in range(len(input_list)):
        j = int(input_list[i] / size)
        if j != len(input_list):
            buckets_list[j].append(input_list[i])
        else:
            buckets_list[len(input_list) - 1].append(input_list[i])

    # Сортируем элементы внутри блоков с помощью сортировки вставкой
    for z in range(len(input_list)):
        vsort(buckets_list[z])
            
    # Объединяем блоки с отсортированными элементами в один список
    final_output = []
    for x in range(len(input_list)):
        final_output = final_output + buckets_list[x]
    if flag == 1:
        for i in range(len(final_output)):
            final_output[i] = final_output[i] - abs(min_value)
    return final_output

#Сортировка вставками
def vsort(bucket):
    for i in range (1, len (bucket)):
        var = bucket[i]
        j = i - 1
        while (j >= 0 and var < bucket[j]):
            bucket[j + 1] = bucket[j]
            j = j - 1
        bucket[j + 1] = var

#Сортировка "троек" в пирамиде
def heapify(array, n, i):
    largest = i
    l = 2 * i + 1
    r = 2 * i + 2

    if l < n and array[i] < array[l]:
        largest = l
    if r < n and array[largest] < array[r]:
        largest = r

    if largest != i:
        array[i], array[largest] = array[largest], array[i]
        heapify(array, n, largest)

#Пирамидальная сортировка
def psort(array):
    n = len(array)
    for i in range(n // 2, -1, -1):
        heapify(array, n, i)
        #print('Первичная сортировка',array,i)
    for i in range(n - 1, 0, -1):
        array[i], array[0] = array[0], array[i]
        heapify(array, i, 0)
        #print("Очередная итерация", array)

    return array