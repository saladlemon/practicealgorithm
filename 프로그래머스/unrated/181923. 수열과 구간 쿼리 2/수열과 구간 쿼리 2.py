def solution(arr, queries):
    sol = []
    for query in queries:
        s, e, k = query
        m = []
        for i in range(s, e+1):
            if arr[i] > k:
                m.append(arr[i])
        if not m:
            sol.append(-1)
        else:
            sol.append(min(m))
    return sol
