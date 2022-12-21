#def calc(s):
#    result = 0
#    per = 0
#    for i in s:
#        if i == "Р":
#            per+=1
#        else:
#            if per>result:
#                result=per
#            else:
#                per=0
#    return result



def calc(s):
    c=0
    p='Р'
    while not(s.count(p)==0):
        c+=1
        p+='Р'
    else:
        return c

print(calc("ОРРООРРРОР"))