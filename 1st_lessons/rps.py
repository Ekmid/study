first_pl, second_pl = input("Введите решение первого и второго игрока в нижнем регистре ЧЕРЕЗ ПРОБЛЕЛ: ").split()

if first_pl == second_pl:
    print ("Вывод: ничья")
elif first_pl == 'камень' and second_pl == 'ножницы':
    print ("Вывод: победил игрок №1")
elif second_pl == 'камень' and first_pl == 'ножницы':
    print ("Вывод: победил игрок №2")
elif second_pl == 'камень' and first_pl == 'бумага':
    print ("Вывод: победил игрок №1")
elif second_pl == 'бумага' and first_pl == 'камень':
    print ("Вывод: победил игрок №2")
elif second_pl == 'ножницы' and first_pl == 'бумага':
    print ("Вывод: победил игрок №2")
elif  second_pl == 'бумага' and first_pl == 'ножницы':
    print ("Вывод: победил игрок №1")
