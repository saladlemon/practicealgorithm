def solution(arr, queries):
    temp = 0
    i = 0
    j = 1
    for f in range(0, len(queries)):
        a = queries[f][i]
        b = queries[f][j]
        temp = arr[a]
        arr[a] = arr[b]
        arr[b] = temp
    return arr
        