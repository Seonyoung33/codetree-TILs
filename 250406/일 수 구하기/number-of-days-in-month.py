n = int(input())

# 출력
if n == 2:
	print("28")
elif n <= 7:
    if n % 2 == 1:
        print("31")
    else:
        print("30")
else:
    if n % 2 == 0:
        print("31")
    else:
        print("30")