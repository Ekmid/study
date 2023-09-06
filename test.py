n = int(input('Введие n: '))

a = n // 3
b = n // 5
c = n // 15

asum = (3 + a * 3) * a / 2
bsum = (5 + b * 5) * b / 2
csum = (15 + c * 15) * c / 2
sum = asum + bsum - csum
print(sum)