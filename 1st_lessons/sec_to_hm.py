seconds = int(input("Введите число секунд: "))

hours = seconds // 3600
seconds = seconds % 3600
minutes = seconds // 60

print(f"{hours} час(а/ов) и {minutes} минут(а/ы)")