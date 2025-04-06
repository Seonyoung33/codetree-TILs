abc = input().split( )
a, b, c = int(abc[0]), int(abc[1]), int(abc[2])

if a > b:
    if b > c:
        print(b)
    elif c > b:
        if a > c:
            print(c)
        else:
            print(a)
elif b > a:
    if a > c:
        print(a)
    elif c > a:
        if b > c:
            print(c)
        else:
            print(b)
