def q1a(a,b):
    return a + b

def q1b(a,b):
    try:
        x = a/b
        print(x)
    except ZeroDivisionError:
        print (None)

def q1c(b,a):
    return (b*a)/2

def q1d(r):
    pi=3,14
    return pi*(r**2)

def q1e(c,h):
    return c/h

def q1f(a,b):
    return a**b

def q2():
    return print("Conceito B, Conceito C, Conceito D")

def q3():
    return print("Conceito B")

def q4():
    return print("A data de hoje nao é 8/5/13")

    

def q5(a,b,c,d,e):
    if a>b and a>c and a>d and a>e:
        return a
    if b>a and b>c and b>d and b>e:
        return b
    if c>a and c>b and c>d and c>e:
        return c
    if d>a and d>b and d>c and d>e:
        return d
    if e>a and e>b and e>c and e>d:
        return e
    
def q6(a):
    for n in range(a):
        print("spam")

def q7(n):
    r = 1
    while r<=n:
        r = r+1
        print("spam")

def q8(n):
    print(1)
    r = 1
    while r<n:
        r = r+2
        if r > n:
            break
        else:
            print(r)

def q9(x,y):
    if x < y:
        r = x
        print(r)
        while r >=x and r < y:
            r = r +1
            if r > y:
                break
            else:
                print(r)

def q_10(x,y):
    if x < y:
        r = x
        print(r)
        while r >=x and r < y:
            r = r + 1
            if r >= y:
                break
            else:
                print(r)
                


def q_11(x,y):
    if x < y:
        r = x
        while r >=x and r < y:
            r = r +1
            if r > y:
                break
            else:
                print(r)

def q_12(x,y):
    if x < y:
        soma = 0
        r = x
        while r <= y:
            soma = soma+r
            r = r + 1
            if r > y:
                print(soma)

def q13(n):
    soma = 0
    r = 0
    while r <= n:
        if r%2==0:
            soma = soma+r
        else:
            soma = soma - r
        r= r+1
    return soma

def q14(a):
    if a > 0:
        n = 1
        for x in range(0,a):
            n = n*(a-x)
        print (n)
def q15():
        n = 1
        for x in range(0,1000000):
            n = n*(1000000-x)
        print (n)
def q22(n):
    if n==0:
        print("Fogo!")
    else:
        print(n)
        q22(n-1)
#Para n = 10 a saida será: 10, 9, 8, 7, 6, 5, 4, 3, 2, 1 Fogo!


##TODAS AS OUTRAS QUE NÃO ESTÃO AQUI EU NÃO CONSEGUI RESPONDER
