def vivod(n):
    for i in range(1,n+1):
        result=1
        for j in range(1,i+1):
            result*=j
        print(result, end=' ')

vivod(5)
