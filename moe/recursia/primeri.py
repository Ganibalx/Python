def fact(num): #Рекурсия факториал
    if num == 0:
        return 1
    else:
        return num*fact(num-1)

print(fact(10))

def degree(a,b): #Рекурсия возведение в степень
    if b == 0:
        return 1
    else:
        return a* degree(a,b-1)

print(degree(2,10))

