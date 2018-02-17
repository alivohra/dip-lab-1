d = {}
x = "As you saw, so shall you reap"
print(x.split())
for i in x.split():
    if i in d.keys():
        d[i] += 1
    else:
        d[i] = 1
print(d)       

