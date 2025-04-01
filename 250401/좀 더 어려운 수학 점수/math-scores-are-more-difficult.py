a = input().split(" ")
b = input().split(" ")

a_math = int(a[0])
a_eng = int(a[1])

b_math = int(b[0])
b_eng = int(b[1])

if a_math > b_math:
    print("A")
elif a_math < b_math:
    print("B")
else:  # a_math == b_math
    if a_eng > b_eng:
        print("A")
    else:
        print("B")
