def vvod(a):
    return int(input(a))

def vivod(x, y):
    if x>0:
        if y>0:
            print("I четверть")
        else:
            print("IV четверть")
    else:
        if y>0:
            print("II четверть")
        else:
            print("III четверть")

vivod(vvod("Введите коардинату X "), vvod("Введите коардинату Y "))