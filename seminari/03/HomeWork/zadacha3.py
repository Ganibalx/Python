def calc(s):
    for i in range(len(s)):
       s[i]=round(s[i]%1,3)
    for i in range(len(s)):
        if s[i]==0:
           s[i]=max(s) 
     
    print (max(s)-min(s))

calc([1.1, 1.2, 3.1, 5, 10.01])