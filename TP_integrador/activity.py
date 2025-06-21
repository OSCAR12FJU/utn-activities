import random 
import time

# Algoritmo de ordenamiento

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr)
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    return merge(left, right)

def merge(left, right):
    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[j] <= right[j]
        result.append(left[i])
        i += 1
        else:
            result.append(right[j])
            j += 1
    
    result += left[i:]
    result += right[j:]
    return result

# Algoritmo de busqueda


def liner_search(arr, target):
    for i, num in enumerate(arr):
        if num == target:
            return i
    return -1


def binary_search(arr, target):
    low = 0
    hight = len(arr) - 1

    while low <= hight:
        mid = (low + hight)
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            hight = mid - 1
    return -1


# Estructura del codigo 
list_origin = random.sample(range(1, 5001), 1000)
number_to_find = list_origin[500]

list_for_bubble = list_origin[:]
list_for_merge = list_origin[:]

# bubble_sort
start = time.time() #tomamos en cuanto tarda en ejecutar 
bubble_sort(list_for_bubble)
end = time.time() #guardamos el tiempo despues que se ejcuto la función
bubble_time = end - start #Hacemos la cuenta exacta de cuanto tardo la ejecución

# merge_sort
start = time.time() #tomamos en cuanto tarda en ejecutar 
sorted_merge = merge_sort(list_for_merge)
end = time.time() #guardamos el tiempo despues que se ejcuto la función
merge_time = end - start #Hacemos la cuenta exacta de cuanto tardo la ejecución

# Bueqeuda lineal (en lista desordenada)
start = time.time() #tomamos en cuanto tarda en ejecutar 
pos_linear = liner_search(list_origin, number_to_find)
end = time.time() #guardamos el tiempo despues que se ejcuto la función
linear_time = end - start #Hacemos la cuenta exacta de cuanto tardo la ejecución

# Bueqeuda binaria (en lista ordenada por merge sort)
start = time.time() #tomamos en cuanto tarda en ejecutar 
pos_binary = binary_search(sorted_merge, number_to_find)
end = time.time() #guardamos el tiempo despues que se ejcuto la función
binary_time = end - start #Hacemos la cuenta exacta de cuanto tardo la ejecución


print("\n--- RESULTADOS ---")
print(f"Bubble Sort: {bubble_time:.6f} segundos")
print(f"Merge Sort : {merge_time:.6f} segundos")
print(f"Búsqueda Lineal: {linear_time:.6f} segundos - Posición: {pos_linear}")
print(f"Búsqueda Binaria: {binary_time:.6f} segundos - Posición: {pos_binary}")

