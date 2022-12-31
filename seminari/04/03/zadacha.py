def prov(s):
    s=s.lower()
    flag=0
    for i in range(len(s)//2):
        if s[i]!=s[-i-1]:
            flag=1
    if flag==0:
        print('Полиндром')
    else:
        print('Не полиндром')

s='Дерд'
prov(s)

# a = input()
# print("палиндром" if a.lower()==a[::-1].lower() else "не палиндром")
