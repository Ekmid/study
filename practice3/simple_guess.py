def guess(root):
    for number in range(1, root):
        if root / number == number:
            print(root / number, 'Вот он с*ка!')
            break
        else:
            print(f'{number} Да где он *ля?')

guess(9821956)