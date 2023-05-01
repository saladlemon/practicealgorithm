def solution(n):
    i = 0
    if n%2 == 1:
        for a in range(1, n+1, 2):
            i += a
    else:
        for a in range(2, n+1, 2):
            i += a**2
    return i
              