def vivod(n):
    for i in range(1,n+1):
        result=1
        for j in range(1,i+1):
            result*=j
        print(result, end=' ')

vivod(5)

def Factorials(n, result = 1):
    if(n<1):
        return result;
    return Factorials(n-1, n*result);

n = int(input('Введите целое число: '));

listFactorials = [];

for i in range(1, n+1):
    listFactorials.append(Factorials(i));

print(listFactorials);
