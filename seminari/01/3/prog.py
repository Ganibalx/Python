def vvod():
    array = [0] * 5
    for i in range(5):
        array[i]=int(input(f'Введите {i} число '))
    return array

def max(array):
    max = array[0]
    for i in range(0 , len(array)):
        if max<array[i]:
            max=array[i]
    return max

print('max= ', max(vvod()))