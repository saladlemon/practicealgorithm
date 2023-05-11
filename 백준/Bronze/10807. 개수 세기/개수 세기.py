N = int(input())
Num = list(map(int, (input().split(" "))))
v = int(input())
s = 0
for i in range(len(Num)):
    if v == Num[i]:
        s = s + 1
print(s)