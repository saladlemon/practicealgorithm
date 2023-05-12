N, M = map(int, input().split())
n = 1
arr = [0]*N
for a in range(N):
    arr[a] = n
    n += 1
for b in range(M):
    i, j = map(int, input().split())
    temp = arr[i-1]
    arr[i-1] = arr[j-1]
    arr[j-1] = temp
result = ' '.join(map(str, arr))
print(result)