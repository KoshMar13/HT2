# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# Пример:
# - 6782 -> 23
# - 0,56 -> 11

inp = str(input('Insert number: '))
sum = 0
for i in inp:
    if i.isdigit():
        sum += int(i)
print(sum)
