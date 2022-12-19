def vvod():
    return int(input())

def vivod(nomer):
    if 0<=nomer<=36:
        if nomer == 0:
            print('зеленый')
        elif 1<=nomer<=10:
            if nomer%2 == 0:
                print('черный')
            else:
                print('красный')
        elif 11<=nomer<=18:
            if nomer%2 == 0:
                print('красный')
            else:
                print('черный')
        elif 19<=nomer<=28:
            if nomer%2 == 0:
                 print('черный')
            else:
                print('красный')
        else:
            if nomer%2 == 0:
                print('красный')
            else:
                print('черный')
    else:
        print('Выход за лимиты')

vivod(vvod())