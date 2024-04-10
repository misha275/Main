n = 1
def f(n):
    return(((n**2+1)**(1/2))/n)
while f(n)-1 >= 5/1000:
    print(n)
    print(f(n)-1)

    n +=1
