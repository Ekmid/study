a: list[int] = [1, 2, 3, 3, 5]
b: list[int] = [0, 0, 1, 0, 1]

answer = [val*b[i] for i, val in  enumerate(a)]
print(answer)
