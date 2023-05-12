N = int(input())
Num = str(input())
Sum = 0
if len(Num) == N:
    for i in range(len(Num)):
        Sum = Sum + int(Num[i])
else:
    print("Wrong Number")
print(Sum)

