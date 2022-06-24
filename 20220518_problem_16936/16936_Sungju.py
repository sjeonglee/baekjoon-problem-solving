import sys
N = int(sys.stdin.readline())
B = list(map(int, sys.stdin.readline().split()))

B_multiply_2 = {b:(b * 2) for b in B if (b * 2) in B}
B_divide_3 = {b:(b // 3) for b in B if (b % 3 == 0) & ((b // 3) in B)}

B_multiply_2.update(B_divide_3) ### union two dicts

x = (set(B) - set(B_multiply_2.values())).pop() ### start value
f = (set(B) - set(B_multiply_2.keys())).pop() ### final value
# print(f'{x}, {f}')

result = []
while(x != f):
  result.append(x)
  x = B_multiply_2[x]
result.append(f)

print(' '.join(map(str, result)))