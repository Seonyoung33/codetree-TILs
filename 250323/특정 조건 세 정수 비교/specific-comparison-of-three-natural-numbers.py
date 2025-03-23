abc = input().split(" ")

a = int(abc[0])
b = int(abc[1])
c = int(abc[2])

if a == min(a, b, c):
    print("1", end=" ")
else:
    print("0", end=" ")

if a==b and b==c:
    print("1")
else:
    print("0")