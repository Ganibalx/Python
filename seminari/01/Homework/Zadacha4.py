def vvod():
    f = False
    while not f:
        result=int(input("Введите номер четверти "))
        if 5>result>0:
            f=True
    return result

def vivod(a):
    if a==1:
        print('X>0, Y>0')
    elif a==2:
        print('X<0, Y>0')
    elif a==3:
        print('X<0, Y<0')
    elif a==4:
        print('X>0, Y<0')

vivod(vvod())