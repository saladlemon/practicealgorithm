H, M = map(int, input().split())
if 0 <= H <= 23 and 0 <= M <= 59:
    if M >= 45:
        print(H, (M-45))
    elif M <45:
        if H == 0:
            print((H+23),(60-(45-M)))
        else:
            print((H-1), (60-(45-M)))