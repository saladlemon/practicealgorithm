L = list(range(1, 10001))
R = list()
for i in L:
    for j in str(i):
        i += int(j)
    if i <= 10000:
        R.append(i)
for n in set(R):
    L.remove(n)
for self in L:
    print(self)
