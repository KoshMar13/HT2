# Дана строка текста, состоящая из букв русского алфавита "О" и "Р".
# Буква О соответсвует выпадению Орла, буква Р - решки.
# Напишите программу, которая подсчитывает наибольшее количество подряд выпавших Решек.

inp = str(input('Введите строку из "О" и "Р" без пробела: '))
count = 0
countMax = 0
for i in inp:
    if i == 'Р':
        count += 1
    else:
        count = 0
    if count > countMax:
        countMax = count
print(countMax)
