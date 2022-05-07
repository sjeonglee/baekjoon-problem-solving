n = input()

try:
  n = int(n)
except ValueError:
  print('ERROR: input int number')

roman = [1, 5, 10, 50]

for i in range(n):
    if i == 0:
        cases = roman
    else:
	    cases = {x+y for x in roman for y in cases}

print(len(cases))

# import sys

# n = int(sys.stdin.readline().strip())

# def calculate_answers(n:int):
#     if n == 1:
#         ans = [1, 5, 10, 50]
#         return ans
#     else:
#         ans = calculate_answers(n - 1)
#         new_ans = []
#         for a in ans.copy():
#             temp1 = a + 1
#             temp2 = a + 5
#             temp3 = a + 10
#             temp4 = a + 50
#             new_ans.extend([temp1, temp2, temp3, temp4])
#         new_ans = list(set(new_ans))
#         return new_ans

# answer = calculate_answers(n)
# print(len(answer))