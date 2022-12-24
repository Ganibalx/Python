def calc(s):
    n=0
    if len(s)%2!=0:
        n=1
    result=[0]*int(((len(s)+n)/2))
    for i in range(len(result)):
        result[i]=s[i]*s[-i-1]
    print (result)

calc([2, 3, 5, 6])