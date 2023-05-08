def solution(start, end):
    arr = []
    ran = end - start + 1
    for i in range(ran):
        arr.append(start)
        start += 1        
    return arr