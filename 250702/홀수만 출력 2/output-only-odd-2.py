a, b = map(int, input().split())

for i in range(a, b - 1, -1):  # b부터 a까지 감소하면서 반복
    if i % 2 == 1:             # 홀수인 경우만 출력
        print(i, end=" ")