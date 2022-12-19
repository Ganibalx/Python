import random
def zap(n):
    result = [0]*n
    for i in range(n):
        result[i] = i+1
    return result

def ran(list):
    n = random.randint(1,len(list))
    x = 0
    y = 0
    p = 0
    for i in range(n+1):
        x = random.randint(0, len(list))
        y = random.randint(0, len(list))
        p = list[x]
        list[x] = list[y]
        list[y] = p
    print(list)


ran(zap(4))