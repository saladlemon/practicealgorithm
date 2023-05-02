def solution(num_list):
    allmul = 1
    allsum = 0
    for i in range(0, len(num_list)):
        allmul = allmul*num_list[i]
        allsum = allsum + num_list[i]
        allsquare = allsum**2
    if allmul < allsquare:
        return 1
    elif allmul > allsquare:
        return 0