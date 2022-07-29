f = []
s = []
for n in range(10):
    i = int(input())
    f.append(int(i%42))
    for j in f:
        if j not in s:
            s.append(j)
print(len(s))