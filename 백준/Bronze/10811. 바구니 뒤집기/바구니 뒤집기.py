N, M = map(int, input().split())
arr = []
n = 1
for a in range(N):
    arr.append(n)
    n += 1
for a in range(M):
    i, j = map(int, input().split())
    first_arr = arr[:i-1]
    middle_arr = arr[i-1:j]
    last_arr = arr[j:]
    change_arr = middle_arr[::-1]
    arr = first_arr + change_arr + last_arr
result = ' '.join(map(str, arr))
print(result)