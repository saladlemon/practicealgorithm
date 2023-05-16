i = 0
arr = []
while True:
    L, P, V = map(int, input().split())
    if L == 0 and P == 0 and V == 0:
        break
    arr.append(((V//P)*L)+min(V % P, L))
    i += 1
for a in range(len(arr)):
    print(f'Case {a+1}: {arr[a]}')

