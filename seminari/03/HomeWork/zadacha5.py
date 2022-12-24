def calc(n):
    fib1=[0]*(n+1)
    fib1[1]=1
    for i in range(2,n+1):
        fib1[i]=fib1[i-1]+fib1[i-2]
    fib2=[0]*(n-1)
    fib2[-1]=-1
    fib2[-2]=-2
    for i in range(-3,-n,-1):
        fib2[i]=fib2[i+1]+fib2[i+2]      
    print(fib2+fib1)

calc(8)