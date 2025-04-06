first = input().split(" ")
second = input().split(" ")
third = input().split(" ")

if str(first[0])=="Y" and int(first[1])>=37:
    if str(second[0])=="Y" and int(second[1])>=37:
        print("E")
    elif str(third[0])=="Y" and int(third[1])>=37:
        print("E")
    else:
        print("N")
elif str(second[0])=="Y" and int(second[1])>=37:
    if str(third[0])=="Y" and int(third[1])>=37:
        print("E")
    else:
        print("N")