# вводится цел. число выводится цифры этого числа
a = int(input())
A = []
while a != 0:
    b = a % 10
    a = int((a - b) / 10)
    A.append(b)
A.reverse()
print(*A)


# 1.1, 1.2, 1.3
# вводится число, выводится кол-во элементов в масиве равных этому числу, равные числа стоящие или не стоящие рядом
# и равные числа строго не стоящие рядом
from random import randint
A = [randint(0, 5) for x in range(5)]
b = int(input())
c = 0
d = 0
e = 0
for i in range(5):
    if A[i] == b:
        print("элемент номер", i + 1, "=", b)
        c += 1
if c == 0:
    print("не найдено таких значений")
for k in range(1, 5):
    if A[k - 1] == A[k]:
        print("числа рядом:", A[k])
        d += 1
if d == 0:
    print("нет равных чисел стоящих рядом")
for l in range(0, 5):
    for f in range(1, 4):
        if A[l] == A[f] and A[f - 1] != A[f] and f != l:
            print("равные числа не стоящие рядом:", A[f])
            e += 1
if e == 0:
    print("нет равных чисел стоящих не стоящих рядом")
print("массив:", *A)


# 2.1
# смещает все эелементы массива в право
from random import randint
A = [randint(0, 9) for x in range(6)]
print(*A)
A = A[-1:] + A[:-1]
print(*A)


# 2.2
# вводится число - кол-во элементов в массиве(лучше четное)  выводится первая часть массива в конце, вторая в начале
from random import randint
n = int(input())
A = [randint(0, 9) for x in range(n)]
print(*A)
B = A[0:n//2]
C = A[n//2:n]
print(*A)
print(*B)
print(*C)
B.reverse()
C.reverse()
print(B+C)


# 2.3
# вводится число - кол-во элементов массива А, выводится массив, где все положительные элементы в начале, а отрицательные в конце(в т.ч. и ноль)
from random import randint
n = int(input())
A = [randint(-100, 100) for x in range(n)]
print(*A)
B = []
C = []
for i in range(n):
    if A[i] > 0:
        B.append(A[i])
    elif A[i] <= 0:
        C.append(A[i])
print(*B)
print(*C)
print(*(B + C))


# казик
from random import randint
a = int(input("введите целое число(для остановки введите 0):"))
B = []
balans = 100
while a != 0 and balans > 10:
    A = [randint(1, 10) for x in range(10)]
    b = 0
    c = 0
    for i in range(10):
        if A[i] == a:
            print("элемент номер", i + 1, "=", a)
            b += 1
            balans += 10
            print("победа +10руб")
            print("баланс:", balans)
            c += 1
    if b == 0:
        balans -= 50
        print("проигрыш -50руб")
        print("баланс:", balans)
        c += 1
    B.append(balans)
    a = int(input("введите целое число(для остановки введите 0):"))
if balans <= 10:
    print("вы проиграли")
    print("максимальный баланс:", max(B))


# игра (дилемма заключенного)
n = int(input("введите количество ходов:"))
print("1 - сотрудничать, 0 - предать")
monA = 0
monB = 0
for i in range(1, n+1):
    print("ход", i, "осталось ходов:", n - i)
    a = int(input("выбор игрока 1:"))
    b = int(input("выбор игрока 2:"))
    if a == 0:
        if b == 0:
            monB += 1
            monA += 1
            print("очки игрока 1:", monA, "очки игрока 2:", monB)
        elif b == 1:
            monA += 5
            monB += 0
            print("очки игрока 1:", monA, "очки игрока 2:", monB)
    elif a == 1:
        if b == 0:
            monB += 5
            monA += 0
            print("очки игрока 1:", monA, "очки игрока 2:", monB)
        elif b == 1:
            monA += 3
            monB += 3
            print("очки игрока 1:", monA, "очки игрока 2:", monB)
if monA > monB:
    print("победил игрок 1")
    print("очки игрока 1:", monA, "очки игрока 2:", monB)
elif monA == monB:
    print("ничья")
    print("очки игрока 1:", monA, "очки игрока 2:", monB)
elif monA < monB:
    print("победил игрок 2")
    print("очки игрока 1:", monA, "очки игрока 2:", monB)


# задача 3.1
# тоже что и ниже но только с + (без -)
a = str(input())
A = a.split("+")
b = 0
print(A)
for i in range(int(len(A))):
    b += int(A[i])
print(b)


# задача 3.2
# тут нужно было чтобы из введенной строки (вид: 67+47+82-87) считалось значение
# p.s. она не работает(
# a = str(input())
# A = []
# b = 0
# summa = 0
# for x in a:
#     A.append(x)
# for i in range(len(A)):
#     if A[i] != "+" and A[i] != "-":
#         b *= 10
#         b += int(A[i])
#     elif A[i] == "+":
#         summa += b
#         b = 0
#     elif A[i] == "-":
#         summa -= b
#         b = 0
# print(A, b)
# print(summa)


# задача 4.1
# вводится несколько слов через пробел выводится только первое слово
a = str(input())
A = a.split(" ")
print(A[0])


# задача 4.2
# меняет расширение для введеного имени файла с расширением
a = str(input())
c = str(input())
A = a.split(".")
b = str()
for i in range(len(A)):
    if i == len(A)-1:
        A.remove(A[i])
        b += c
    else:
        b += A[i]
        b += "."
print(A)
print(b)


# задача 5.1
# есть алфавит из 4х букв на вход число - склько в слове букв    на выход - все комбинации и их количество
# частично работает)
n = int(input())
A = ["Ш", "Ы", "Ч", "О"]
s = str()
b = 0
for j in range(len(A)):
    s += A[j]
    for k in range(len(A)):
        s += A[k]
        for f in range(len(A)):
            s += A[f]
            for l in range(len(A)):
                s += A[l]
                if s[1:-2] == "Ы":
                    print(s)
                    b += 1
                s = s[:-1]
            s = s[:-1]
        s = s[:-1]
    s = s[:-1]
print(b)

# задачи на работу с файлами 
# задача 1.1
fl = open("first_file.txt")
s = fl.readlines()
summa = 0
for i in range(len(s)):
    summa += int(s[i][:-1])
print(summa/len(s))
print(s)
fl1 = open("second_file.txt")
fl1.write("summa/len(s)".format(summa, len(s), summa/len(s)))

