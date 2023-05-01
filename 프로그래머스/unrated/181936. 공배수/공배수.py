def solution(number, n, m):
    a = 0
    if number%n == 0 and number%m == 0:
        a = 1
    return a