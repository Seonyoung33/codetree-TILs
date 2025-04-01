a = int(input().split(" "))
b = input().split(" ")

a_math = a.array[0]
a_eng = int(a.array[1])

b_math = int(b.array[0])
b_eng = int(b.array[1])

if a_math > b_math:
    print("A")
else:
    print("B")

if a_math == b_math:
    if a_eng > b_eng:
        print("A")
    else:
        print("B")