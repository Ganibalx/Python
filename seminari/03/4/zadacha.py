flag = 0
p='text.txt'
data=open(p,'a')
while flag == 0:
    stroka=input()
    if len(stroka)!=0:        
        data.write(f'{stroka} \n')        
    else:
        flag=1
data.close