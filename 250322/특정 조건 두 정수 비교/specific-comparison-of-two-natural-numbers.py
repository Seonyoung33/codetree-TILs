inp = input()

array = inp.split(" ")

a = int(array[0])
b = int(array[1])

if a<b :
    print("1", end = " ")
else:
    print("0", end = " ")

if a==b:
    print("1")
else:
    print("0")