N = input().lower()
Nl = list(set(N))
L = []
for i in Nl:
    cnt = 0
    for j in N:
        if i == j:
            cnt += 1
    L.append(cnt)
max_alpha = L.index(max(L))
Max = max(L)
del L[max_alpha]
remove = [x for x in L if x != Max]
if len(remove) < len(L):
    print("?")
else:
    print(Nl[max_alpha].upper())