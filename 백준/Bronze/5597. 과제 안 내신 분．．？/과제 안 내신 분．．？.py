arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]
for i in range(28):
    n = int(input())
    arr = [x for x in arr if x != n]
print(arr[0])
print(arr[1])
