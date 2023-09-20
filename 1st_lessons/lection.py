a, b, c = input("Введите три числа: ").split()
a, b, c = float(a), float(b), float(c)
text = input('Введите строку: ')

print(f"{text} {a}, {b}, {c}")
print(a + b + c)
print(a**(b**c))