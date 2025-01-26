# разбиение числа на цифры
def razb(a):
    b = str(a)
    A = []
    for i in range(len(b)):
        A.append(b[i])
    return A



# перевод из числа из системы счисления x в систему счисления n
def per(sch, ss1, ss2):
    vr1 = int(str(sch), ss1)
    vr2 = ''
    while vr1 != 0:
        vr2 += str(vr1%ss2)
        vr1 //= int(ss2)
    vr2 = vr2[::-1]
    return vr2

# проверяет является ли число простым
def prost(a):
    b = 0
    for k in range(1, int(a)):
        if a%k == 0:
            b += 1
    if b <= 1:
        return a
