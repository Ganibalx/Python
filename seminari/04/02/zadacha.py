def calc(s):
    list=s.split(' ')    
    for i in range(0, len(list)-1, 2):        
        list[i],list[i+1]= list[i+1],list[i]        
    result=' '.join(list)
    print(result)
    
s='5 4 3 2 1'
print(s)
calc(s)

# s = list(map(int, input().split()))
# s[:-1:2], s[1::2] = s[1::2], s[:-1:2]
# print(*s)
