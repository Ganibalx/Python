def vivod(n):
    s= str(n)
    result=0
    for i in s:
        if not(i == "."):
            result+=int(i)
    return result

print(vivod(0.56))