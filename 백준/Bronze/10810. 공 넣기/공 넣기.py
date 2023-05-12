N, M = map(int, input().split())
arr = [0]*N
for a in range(M):
    i, j, k = map(int, input().split())
    for b in range(i-1,j):
        arr[b] = k
result = ' '.join(map(str, arr)) 
print(result)