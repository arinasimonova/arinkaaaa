Python 3.11.9 (tags/v3.11.9:de54cf5, Apr  2 2024, 10:12:12) [MSC v.1938 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import re
... 
... def execute_command(command, array):
...     if not isinstance(array, list):
...         return "Переданный аргумент не является массивом"
...     
...     match_index = re.match(r"Получить элемент по (\d+) индексу", command)
...     if match_index:
...         index = int(match_index.group(1))
...         if 0 <= index < len(array):
...             return array[index]
...         else:
...             return "Индекс выходит за пределы массива"
...     
... 
...     match_interval = re.match(r"Получить элементы с (\d+) по (\d+) с шагом (\d+)", command)
...     if match_interval:
...         start, end, step = map(int, match_interval.groups())
...         if start < 0 or end > len(array) or step <= 0:
...             return "Некорректный шаг или интервал"
...         return array[start:end:step]
...     
... 
...     match_from_end = re.match(r"Получить (\d+)-й элемент с конца массива", command)
...     if match_from_end:
...         index_from_end = int(match_from_end.group(1))
...         if 1 <= index_from_end <= len(array):
...             return array[-index_from_end]
...         else:
...             return "Индекс выходит за пределы массива"
...     
...     return "Неподдерживаемая команда"
... 
... 
... 
arr = [10, 23, 54, 78, 91, 34, 67, 88]
print(execute_command("Получить элемент по 4 индексу", arr))          # Ожидаемый результат: 91
print(execute_command("Получить элементы с 2 по 7 с шагом 2", arr))  # Ожидаемый результат: [54, 91, 67]
print(execute_command("Получить 3-й элемент с конца массива", arr))  # Ожидаемый результат: 67
print(execute_command("Получить 2-й элемент с конца массива", arr))  # Ожидаемый результат: 88
