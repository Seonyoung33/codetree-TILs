a = input().split(" ")
b = input().split(" ")

aMath = int(a[0])
aEnglish = int(a[1])

bMath = int(b[0])
bEnglish = int(b[1])

if aMath>bMath and aEnglish>bEnglish:
    print("1")
else:
    print("0")