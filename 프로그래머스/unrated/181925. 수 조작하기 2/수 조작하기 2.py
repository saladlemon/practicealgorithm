def solution(numLog):
    st = ""
    for i in range(1,len(numLog)):
        if numLog[i] - numLog[i-1] == 1:
            st = st + "w"
        elif numLog[i] - numLog[i-1] == -1:
            st = st + "s"
        elif numLog[i] - numLog[i-1] == 10:
            st = st + "d"
        elif numLog[i] - numLog[i-1] == -10:
            st = st + "a"
    return st
            