def calc(s):
    result=0
    for i in range(1,len(s),2):
        result+=s[i]
    print (result)

calc([2, 3, 5, 9, 3])
