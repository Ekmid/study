# import math

# def guess(num: int) -> int:
#     root = math.sqrt(num)

#     if type(root == float):
#         print('НЕ ЦЕЛЫЙ КОРЕНЬ')
#     else: print(root)

# guess(5)

root = 0

def guess(root):
    numbers = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18]
    for number in numbers:
        if root / number == number:
            print(root / number)
            break
        else:
            print(f'{number} НЕ ПОДОШЛО')

guess(9)