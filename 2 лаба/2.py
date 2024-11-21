Python 3.11.9 (tags/v3.11.9:de54cf5, Apr  2 2024, 10:12:12) [MSC v.1938 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import time
... import random
... 
... def quick_sort(arr):
...     if len(arr) <= 1:
...         return arr
...     pivot = arr[-1]
...     left = [x for x in arr[:-1] if x < pivot]
...     right = [x for x in arr[:-1] if x >= pivot]
...     return quick_sort(left) + [pivot] + quick_sort(right)
... 
... def bubble_sort(array):
...     length = len(array)
...     for i in range(length):
...         for j in range(length - i - 1):
...             if array[j] > array[j + 1]:
...                 array[j], array[j + 1] = array[j + 1], array[j]
...     return array
... 
... # Массив для тестирования
... large_data = [random.randint(1, 10000) for _ in range(1000000)]
... small_data = [random.randint(1, 10000) for _ in range(1000)]  # Для пузырьковой сортировки
... 
... # Быстрая сортировка
... start = time.time()
... sorted_quick = quick_sort(large_data.copy())
... quick_sort_duration = time.time() - start
... print(f"Время выполнения быстрой сортировки: {quick_sort_duration:.6f} секунд")
... 
... # Пузырьковая сортировка
... start = time.time()
... sorted_bubble = bubble_sort(small_data.copy())
... bubble_sort_duration = time.time() - start
... print(f"Время выполнения сортировки пузырьком (на меньшем массиве): {bubble_sort_duration:.6f} секунд")
