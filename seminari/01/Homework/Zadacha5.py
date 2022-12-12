def vvod(a):
    result = [0]*2
    for i in range(2):       
        result[i]=int(input(f'Введите коардинату {i+1} точки {a} '))        
    return result

def calculation(a, b):
    print(f'Расстояние между точками - {round((((a[0]-b[0])**2)+((a[1]-b[1])**2)) ** 0.5, 2)}')

calculation(vvod('A'), vvod('B'))  
