while True:
    try:
        first_number = int(input('Введите первое число: '))
        second_number = int(input('Введите второе число: '))
        print(first_number + second_number)
    except ValueError:
        continue