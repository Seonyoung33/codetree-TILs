inp = input()
array = inp.split(" ")

a = int(array[0])
b = int(array[1])

if a>b :
    print(a*b)
else:
    print(b//a)