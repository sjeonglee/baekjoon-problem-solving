# import sys
# import numpy as np

# size_input = sys.stdin.readline().split()
# size_input = [int(e) for e in size_input]

# mtx_input = [sys.stdin.readline().strip() for _ in range(size_input[0])]

# def convert_to_binary(line):
#   return [1 if e=='*' else 0 for e in line]

# mtx_binary = list(map(convert_to_binary, mtx_input))
# mtx_binary = np.array(mtx_binary)

# #### Check whether input is correct
# if not size_input==list(mtx_binary.shape):
#   print('ERROR IN INPUT')

# #### Shrink matrix size
# col_sum = np.sum(mtx_binary, axis=0)
# row_sum = np.sum(mtx_binary, axis=1)

# col_start = min(np.where(col_sum>0)[0])
# col_end = max(np.where(col_sum>0)[0])
# row_start = min(np.where(row_sum>0)[0])
# row_end = max(np.where(row_sum>0)[0])

# mtx = np.copy(mtx_binary)[row_start:(row_end+1), col_start:(col_end+1)]
# size = list(mtx.shape)

# #### Make square lens
# r = int(max(size) / 2)
# l = r * 2 + 1
# mtx_dummy = np.zeros_like(mtx)
# answers = []
# while l>=3:
#   lens = np.zeros((l, l))
#   lens[r] = 1
#   lens[:, r] = 1

#   for i in range(size[0]-l+1):
#     for j in range(size[1]-l+1):
#       if not (mtx[i:(i+l), j:(j+l)]-lens==np.full((l, l), -1)).any():
#         answers.append([i+r+1+row_start, j+r+1+col_start, r])
#         mtx_dummy[i:(i+l), j:(j+l)] = mtx_dummy[i:(i+l), j:(j+l)] + lens
        
#   r -= 1
#   l = r * 2 + 1

# mtx_dummy = np.where(mtx_dummy > 0, 1, 0)
# if (mtx==mtx_dummy).all():
#   print(len(answers))
#   for a in answers:
#     print(' '.join(map(str, a)))
# else:
#   print(-1)


#### Only with basic python
import sys

size_input = sys.stdin.readline().split()
size_input = [int(e) for e in size_input]

mtx_input = [sys.stdin.readline().strip() for _ in range(size_input[0])]

def convert_to_binary(line):
  return [1 if e=='*' else 0 for e in line]

mtx_binary = list(map(convert_to_binary, mtx_input))

#### Check whether input is correct
if not (size_input[0]==len(mtx_binary) and size_input[1]==len(mtx_binary[0])):
  print('ERROR IN INPUT')

# #### Shrink matrix size
# col_sum = [sum() for ] np.sum(mtx_binary, axis=0)
# row_sum = [sum(r) for r in mtx_binary]

# col_start = min(np.where(col_sum>0)[0])
# col_end = max(np.where(col_sum>0)[0])
# row_start = min(np.where(row_sum>0)[0])
# row_end = max([col_sum>0][0])

# mtx = np.copy(mtx_binary)[row_start:(row_end+1), col_start:(col_end+1)]
# size = list(mtx.shape)

#### Make square lens
r = int((max(size_input)-1) / 2)
l = r * 2 + 1
mtx_dummy = [[0 for i in range(size_input[1])] for j in range(size_input[0])]
answers = []
while l>=3:
  lens = [[1 if ((i==r) or (j==r)) else 0 for i in range(l)] for j in range(l)]

  for x in range(size_input[1]-l+1):
    for y in range(size_input[0]-l+1):
      bools = [[mtx_binary[y+j][x+i]==lens[j][i] if ((i==r) or (j==r)) else True for i in range(l)] for j in range(l)]
      if all([all(row) for row in bools]):
        answers.append([y+r+1, x+r+1, r])
        for j in range(l):
          for i in range(l):
            mtx_dummy[y+j][x+i] = mtx_dummy[y+j][x+i] + lens[j][i]
        
  r -= 1
  l = r * 2 + 1

mtx_dummy = [[1 if mtx_dummy[j][i] > 0 else 0 for i in range(size_input[1])] for j in range(size_input[0])]

if mtx_binary==mtx_dummy:
  print(len(answers))
  for a in answers:
    print(' '.join(map(str, a)))
else:
  print(-1)