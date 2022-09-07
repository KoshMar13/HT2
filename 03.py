# Задайте список из n чисел последовательности (1 + 1/N)^N и выведите на экран их сумму.

N = int(input('Insert number: '))
ans = list()

sum = 0
for i in range(1, N + 1):
    sum = int(sum + round((1 + 1/i) ** i, 0))
    ans.append(sum)
print(f'If N = {N}, then answer is: {list(enumerate(ans, start=1))}')
