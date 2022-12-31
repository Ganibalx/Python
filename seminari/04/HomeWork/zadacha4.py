import random

def kof():
    return random.randint(0,100)

k=2
result=''
for i in range(k,-1,-1):
    a=kof()
    if a!=0:
        if i!=0:
            result+=f'+{a}x^{i}'
        else:
            result+=f'+{a}'
result+='=0'
data=open('zadacha4.txt','a')
data.write(result)
data.close
