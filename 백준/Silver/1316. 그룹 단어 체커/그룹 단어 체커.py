N = int(input())
cnt = N
for i in range(N):
    W = input()
    for j in range(len(W)-1):
        if W[j] != W[j+1]:
            if W[j] in W[j+1:]:
                cnt -= 1
                break
print(cnt)