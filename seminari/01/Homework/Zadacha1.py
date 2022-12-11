def vvod():
    return int(input('Введите номер дня недели '))

def vivod(a):
    if a==6 or a==7:
        print("Выходной")
    else:
        print('Не выходной')

vivod(vvod())