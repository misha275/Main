# номер 1
for i in range(10, 1000):
    a = i
    b = int(str(i)[-1] + str(i)[:-1])
    if a % 2 == 0 and a % 5 != 0 and b % 2 != 0 and b % 5 == 0:
        print(a)
        break
# ответ: 52



# номер 5
import math
a = 10
for x in range(1,100):
    for y in range(1, 100):
        for z in range(1, 100):
            if (12 * math.factorial(x) + 2 * math.factorial(y) == math.factorial(z)):
                print(x, y, z)
# ответ:
# 1 3 4
# 3 4 5
# 13 13 14
