def vvod():
    return int(input())

def calc(s):
    result=0
    for i in range(len(s)):
        if s[i]==5:
            result+=1
    print(result)

s=[0]*10
for i in range(len(s)):
    s[i]=vvod()
calc(s)