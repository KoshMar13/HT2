# Реализуйте алгоритм перемешивания списка.

import random
inp = list(map(str, input().split()))
random.shuffle(inp)
print(*inp)
