def solution(l, r):
    result = []
    for i in range(l, r+1):
        contains_5_or_0 = True
        for digit in str(i):
            if digit != '5' and digit != '0':
                contains_5_or_0 = False
                break
        if contains_5_or_0:
            result.append(i)
    return result if result else [-1]
