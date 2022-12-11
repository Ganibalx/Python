def vvod():
    return float(input())

def vivod(a):
    b = int(a*10%10)
    if b!=0:
        print(b)
    else:
        print('нет')

vivod(vvod())