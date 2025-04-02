import random
import math

def RANDOM_0_1():
    return random.randint(0, 1)

def RANDOM(a, b):
    r = b - a + 1             # 欲しい値の数（例：3〜5なら3通り）
    k = math.ceil(math.log2(r))  # 必要なビット数（2^k >= 3）

    while True:
        x = 0
        for _ in range(k):
            x = (x << 1) | RANDOM_0_1()  # kビットの整数を作る
        if x < r:
            return a + x

for _ in range(10):
    print(RANDOM(3, 5), end=' ')

