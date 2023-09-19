# import math

# def guess(num: int) -> int:
#     root = math.sqrt(num)

#     if type(root == float):
#         print('НЕ ЦЕЛЫЙ КОРЕНЬ')
#     else: print(root)

# guess(5)

def guess(root):
    for number in range(1, root+1):
        if root / number == number:
            print(root / number, 'Вот он с*ка!')
            break
        else:
            print(f'{number} СЛОЖНА СЛОЖНА')

guess(1)