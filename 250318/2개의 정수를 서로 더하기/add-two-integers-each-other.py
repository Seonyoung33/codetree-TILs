inp = input()
array = inp.split(" ")

a = int(array[0])
b = int(array[1])

a += b
b += a

print(f"{a} {b}")