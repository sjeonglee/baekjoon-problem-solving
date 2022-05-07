############### HEURISTIC ####

import string
alphabet = list(string.ascii_lowercase)
number = list(map(str, range(10)))

structure = list(input('input: '))
structureReal = [alphabet if s=='c' else number for s in structure]

for i in range(len(structureReal)):
  if i==0:
    carNum = structureReal[i]
  else: # 모든 조합 생성
    carNum = [c+x for c in carNum for x in structureReal[i]]

for c in list(carNum):
  if len(set(c))==len(c): # 중복된 경우가 없는 경우
    pass
  else:
    for x in set(c):
      idx = [i for i, e in enumerate(c) if e==x]
      if len(idx)==1:
        pass
      elif any([a-b==1 for a, b in zip(idx[1:], idx[:-1])]):
        carNum.remove(c)
        break
      else:
        pass


print(len(carNum))



############### MATHMATICAL ####
import string
alphabet = list(string.ascii_lowercase)
number = list(map(str, range(10)))

# def allCases(structure):
#   return math.prod([len(alphabet) if s=='c' else len(number) for s in structure])


# structure = list(input('input: '))
answer = 1
overlap_flag = False
right_before = None

for s in structure:
    if right_before == s:
        overlap_flag = True
    if s == "c" and overlap_flag == False:
        answer = answer * len(alphabet)
        right_before = "c"
    elif s == "c" and overlap_flag == True:
        answer = answer * (len(alphabet)-1)
        right_before = "c"
    elif s == "d" and overlap_flag == False:
        answer = answer * len(number)
        right_before = "d"
    else:
        answer = answer * (len(number)-1)
        right_before = "d"
        
    overlap_flag = False

print(answer)