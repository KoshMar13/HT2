# Задайте список из N элементов, заполненных числами из промежутка[-N, N].
# Найдите произведение элементов на указанных позициях.
# Позиции хранятся в файле file.txt в одной строке одно число.

from random import randint

finp = open('file.txt', 'w')
N = int(input('Insert number: '))
inp = list()
for i in range(N):
    inp.append(randint(N * (-1), N))
print(*inp)

for i in range(N):
    finp.write(str(randint(1, N - 1)) + '\n')
finp.close()

finp = open('file.txt', 'r')
ans = 1
for line in finp:
    ans *= inp[int(line)]
finp.close()

print(ans)
