def solution(str1, str2):
    length = len(str1+str2)
    a = 0
    b = 0
    arr = [None]*length
    for i in range(length):
        if i%2 == 0:
            arr[i] = str1[a]
            a += 1
        elif i%2 != 0:
            arr[i] = str2[b]
            b += 1
    result = ''.join(arr)
    return result