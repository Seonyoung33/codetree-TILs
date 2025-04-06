abc = input().split(" ")

a = int(abc[0])
b = int(abc[1])
c = int(abc[2])

if (a >= b and b >= c) or (a >= c and c >= b):
    print(a)
elif (b >= a and a >= c) or (b >= c and c >= a):
    print(b)
elif (c >= b and b >= a) or (c >= a and a >= b):
    print(c)