import math

def is_integer(n):
    return math.isclose(math.floor(n), n)

def get_integer():
    while True:
        num = input().strip()
        if num.isdigit():
            return int(num)
        print("Пожалуйста, введите целое число.")

def print_numbers_between(a, b):
    if a > b:
        a, b = b, a
    
    current_number = a + 1
    while current_number <= b:
        print(current_number)
        current_number += 1

# Ввод двух чисел от пользователя
a = get_integer()
b = get_integer()

print_numbers_between(a, b)