H, W = map(int, input().strip().split())
N = int(input().strip())
R = []
C = []

for i in range(N):
    square = input().strip().split()
    R.append(int(square[0]))
    C.append(int(square[1]))


def is_in_height(H, W, r, c):
    # return if it is in & if r is height
    if H > r and W > c:
        return True, True
    elif H > c and W > r:
        return True, False
    else:
        return False, False


is_in_height(H, W, r, c)