<<<<<<< HEAD
# import math

# def guess(num: int) -> int:
#     root = math.sqrt(num)

#     if type(root == float):
#         print('НЕ ЦЕЛЫЙ КОРЕНЬ')
#     else: print(root)

# guess(5)

=======
>>>>>>> c5c40bb2797055e8420f21a1998776561e4b8a7d
def guess(root):
    for number in range(1, root):
        if root / number == number:
            print(root / number, 'Вот он с*ка!')
            break
        else:
<<<<<<< HEAD
            print(f'{number} СЛОЖНА СЛОЖНА')
=======
            print(f'{number} Да где он *ля?')
>>>>>>> c5c40bb2797055e8420f21a1998776561e4b8a7d

guess(9821956)