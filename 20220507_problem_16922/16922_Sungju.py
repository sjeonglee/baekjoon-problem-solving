n = input()

try:
  n = int(n)
except ValueError:
  print('ERROR: input int number')


#### MATHEMATICAL ####
# print(sum([j*(j+1)/2 for j in range(n+2)]))

roman = [1, 5, 10, 50]
cases = {0}

for i in range(n):
  cases = {x+y for x in roman for y in cases}

print(len(cases))