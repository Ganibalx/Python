def vivod(s):
    etalon='anton'
    flag=0
    for i in s:
        if i == etalon[flag]:
            flag+=1            
    if flag == (len(etalon)):
        print('заражен')
    else:
        print('не заражен')

vivod('0000a0000n00t00000o000000n')