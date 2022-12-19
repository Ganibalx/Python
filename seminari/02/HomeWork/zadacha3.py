import random
def vivod(n):
    list = [0]*n
    for i in range(len(list)):
        list[i] = random.randint(-n,n)
        print(list[i])
    return list

lst2=[1,2]
lst1= vivod(4)
print(lst1[lst2[0]]*lst1[lst2[1]])
