import sys

size_background = list(map(int, sys.stdin.readline().split()))
H = size_background[0]
W = size_background[1]
N = int(sys.stdin.readline())
size_sticker = []
for _ in range(N):
  size_sticker.append(list(map(int, sys.stdin.readline().split())))

area_max = 0
for i, sticker1 in enumerate(size_sticker):
  for j, sticker2 in enumerate(size_sticker[i+1:]):
    R1 = sticker1[0]
    C1 = sticker1[1]
    R2 = sticker2[0]
    C2 = sticker2[1]
    area_sum = R1*C1 + R2*C2

    ## include the 90 degree rotation case
    MIN = min(H, W)
    MAX = max(H, W)

    if (R1+R2 <= MIN and max(C1, C2) <= MAX) and area_sum > area_max:
      area_max = area_sum
    elif (R1+R2 <= MAX and max(C1, C2) <= MIN) and area_sum > area_max:
      area_max = area_sum
    elif (C1+C2 <= MIN and max(R1, R2) <= MAX) and area_sum > area_max:
      area_max = area_sum
    elif (C1+C2 <= MAX and max(R1, R2) <= MIN) and area_sum > area_max:
      area_max = area_sum
    elif (R1+C2 <= MIN and max(R2, C1) <= MAX) and area_sum > area_max:
      area_max = area_sum
    elif (R1+C2 <= MAX and max(R2, C1) <= MIN) and area_sum > area_max:
      area_max = area_sum
    elif (R2+C1 <= MIN and max(R1, C2) <= MAX) and area_sum > area_max:
      area_max = area_sum
    elif (R2+C1 <= MAX and max(R1, C2) <= MIN) and area_sum > area_max:
      area_max = area_sum
    else:
      continue

print(area_max)
