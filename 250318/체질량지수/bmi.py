inp = input()
array = inp.split(" ")

h = int(array[0])
w = int(array[1])
b = (10000*w) // (h*h)

print(f"{b:.0f}")
if b>=25 :
    print("Obesity")