# from random import randint
# A = [randint(0, 5) for x in range(5)]
# b = int(input())
# c = 0
# d = 0
# e = 0
# for i in range(5):
#     if A[i] == b:
#         print("элемент номер", i + 1, "=", b)
#         c += 1
# if c == 0:
#     print("не найдено таких значений")
# for k in range(1, 5):
#     if A[k - 1] == A[k]:
#         print("числа рядом:", A[k])
#         d += 1
# if d == 0:
#     print("нет равных чисел стоящих рядом")
# for l in range(0, 5):
#     for f in range(1, 4):
#         if A[l] == A[f] and A[f - 1] != A[f] and f != l:
#             print("равные числа не стоящие рядом:", A[f])
#             e += 1
# if e == 0:
#     print("нет равных чисел стоящих не стоящих рядом")
# print("массив:", *A)



# from random import randint
# A = [randint(0, 9) for x in range(6)]
# print(*A)
# A = A[-1:] + A[:-1]
# print(*A)



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
