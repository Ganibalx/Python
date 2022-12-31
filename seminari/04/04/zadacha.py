str = input().split(" ")
d = {}
for x in str:
    key = x[0:2]
    if key not in d.keys():
        d[key] = [x]
    else:
        d[key] += [x]
print(*sorted(d.items()))
