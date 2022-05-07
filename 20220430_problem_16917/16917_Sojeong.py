import sys

input = sys.stdin.readline().strip().split(" ")
A = int(input[0])
B = int(input[1])
C = int(input[2])
X = int(input[3])
Y = int(input[4])

max = max([X, Y]) # 반반 0개부터 둘 중 큰 것에 맞추어서 반반을 살 때까지 iteration
price = 0
for i in range(0, 2 * max + 2, 2):    # i는 반반의 개수
    if i == 0:
        price = A * X + B * Y
        continue
    else:
        x = X - i / 2            # 구매하는 양념 수
        y = Y - i / 2            # 구매하는 후라이드 수
        if x >= 0 and y >= 0:
            temp_price = A * x + B * y + C * i
        elif x >= 0 and y < 0:
            temp_price = A * x + C * i
        elif x < 0 and y >= 0:
            temp_price = B * y + C * i
        else:
            temp_price = C * i

        if temp_price > price:
            continue
        else:
            price = temp_price
print(int(price))