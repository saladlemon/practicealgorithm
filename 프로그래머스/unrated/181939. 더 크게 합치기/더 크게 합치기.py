def solution(a, b):
    re1 = int(str(a)+str(b))
    re2 = int(str(b)+str(a))
    if re1 >= re2:
        answer = re1
    elif re1 < re2:
        answer = re2
    return answer