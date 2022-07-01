A = int(input())
B = int(input())
C = A*(B%10)
D = (A*((B%100)-(B%10)))/10
E = A*(B-(B%100))/100
F = A*B
print("%d\n%d\n%d\n%d\n" % (C,D,E,F))#문자열 출력, 자료형 짝 맞추기