def calc(text):
    result = 0
    for i in range(len(text)):
        result +=60
    return result

def vivod (stoimost):
    print(f'{stoimost//100} р. {stoimost%100} коп.')

vivod (calc('Привет, как дела?!'))