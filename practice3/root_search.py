def guess(root):
    for number in range(1, root):
        if root / number == number:
            print(root / number, 'Попался, гадёныш!')
            break
        else:
            print(f'{number} Да где он ёмае?')

guess(1)