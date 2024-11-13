def find_max_number(b, c):
    a = int(input("Введите число a: "))

    if a > 0:
        макс_число = max(a, b, c)
        return макс_число
    else:
        return -1

b = 5
c = 7
result = find_max_number(b, c)
print("Result:", result)
