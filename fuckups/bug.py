def ab_to_int(a: int | float, b: int | float) -> int | float:
    a, b = a(int | float), b(int | float)
    return a / b


while True:
    a, b = input('Введите два числа для их суммы: ').split()
    try:
        division_score = ab_to_int
    except:
        print('Дружище, ты дурак, введи числа!')
        print()
    except ZeroDivisionError as e:
        print('Дружище, давай без нулей')

    ab_sum = a + b
    print(f'Деление {a} / {b} = {division_score}')
    print()

# Если вдруг это кто-то будет читать, 
# то знайте что я в моменте забил на тайпинг
# и начал просто смотреть на экран