def calc(s):
    list=s.split(' ')
    result=0
    for i in range(1,len(list)):
        if list[i]>list[i-1]:
            result+=1
    return result


s='5 4 3 2 1'
print(calc(s))