import math
def vvod():
    flag=False
    while not flag:
        n=input('Введите точность: ')
        prov=float(n)
        if 10**(-10)<=prov<=10**(-1):
            flag=True
    return n 

print(round(math.pi, len(vvod().split('.')[-1])))