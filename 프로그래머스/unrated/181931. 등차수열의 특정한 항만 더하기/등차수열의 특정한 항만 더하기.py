
def solution(a, d, included):
    r = 0
    for i in range(0, len(included)):
        if included[i] == True:
            r = r + a +(i*d)
    return r
