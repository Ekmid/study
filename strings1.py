# while True:
#     bob_index = words.lower().find('bob')
#     if bob_index == -1:
#         break
#     else:
#         words = words.lower().replace('bob', 'gregory')
#         print(words)
#         break

_list: list = [1, 2, 3]
_str: str = '123'
_tuple: tuple = (
    [1,2],
    [3,9],
    [5,6],
)

# 3 - 5

_list[-1] = 5
_tuple[1][1] = 5

print(_list, _str, _tuple)