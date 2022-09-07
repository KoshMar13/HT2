# Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
# Пример:
# - пусть N = 4, тогда[1, 2, 6, 24](1, 1*2, 1*2*3, 1*2*3*4)

def Factorial(numb):
    if numb == 1:
        return 1
    else:
        return numb * Factorial(numb - 1)


N = int(input('Insert number: '))
ans = list()

for i in range(1, N+1):
    ans.append(Factorial(i))
print(f'If N = {N}, then answer is: {ans}')
