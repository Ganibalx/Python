def Factor(n):
    Ans = []
    d = 2
    while d * d <= n:
        if n % d == 0:
            Ans+=str(d)
            n //= d
        else:
            d += 1
    if n > 1:
        Ans+=str(n)
    return Ans
print(Factor(int(input())))