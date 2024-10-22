def main():
    total = 0
    
    while True:
        number = input("Введите число или 'stop'/'end': ")
        
        if number == 'stop' or number == 'end':
            break
            
        try:
            number = int(number)
            total += number
        except ValueError:
            print("Ошибка! Пожалуйста, введите целое число.")

    print(f"Сумма всех введенных чисел равна {total}")

if __name__ == "__main__":
    main()