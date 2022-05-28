calculation = int(input().strip())
series = list(map(int, input().strip().split(" ")))

def get_two_three(x:int):
    f = {2:0, 3:0}
    
    while x % 2 == 0:
        f[2] = f[2] + 1                 # x가 2로 나눠질 경우 2의 인수 하나 늘리기
        x = x / 2
    
    while x % 3 == 0:
        f[3] = f[3] + 1
        x = x / 3
    return [f[2], f[3]]

# print(factorization(24))

# do factorization
fact = []
for s in series:
    fact.append(get_two_three(s))
fact_copy = fact.copy()

# print("This is fact")
# print(fact)

# get answer
ans = []
for f in fact:
    # 곱2
    gob2 = [f[0] + 1, f[1]]
    if gob2 in fact:
        ans.append(fact.index(f))
        ans.append(fact.index(gob2))
        fact_copy.remove(f)
        fact_copy.remove(gob2)
        break
    na3 = [f[0], f[1] - 1]
    if na3 in fact:
        ans.append(fact.index(f))
        ans.append(fact.index(na3))
        fact_copy.remove(f)
        fact_copy.remove(na3)
        break

nums = len(ans)


while True:
    if len(fact_copy) == 0:
        break
    # print("The num is ", nums)
    # print(ans)
    # front
    gob2_inverse = [fact[ans[0]][0] - 1, fact[ans[0]][1]]
    # print("gob2 inverse")
    # print(gob2_inverse)
    na3_inverse = [fact[ans[0]][0], fact[ans[0]][1] + 1]
    # print("na3 inverse")
    # print(na3_inverse)
    if gob2_inverse in fact:
        ans.insert(0, fact.index(gob2_inverse))
        fact_copy.remove(gob2_inverse)
        # print("I am in gob2 inverse")
        continue
    if na3_inverse in fact:
        ans.insert(0, fact.index(na3_inverse))
        fact_copy.remove(na3_inverse)
        # print("I am in na3 inverse")
        continue
    
    # back
    gob2 = [fact[ans[-1]][0] + 1, fact[ans[-1]][1]]
    # print("gob2")
    # print(gob2)
    na3 = [fact[ans[-1]][0], fact[ans[-1]][1] - 1]
    # print("na3")
    # print(na3)
    if gob2 in fact:
        ans.append(fact.index(gob2))
        fact_copy.remove(gob2)
        # print("I am in gob2")
        continue
    if na3 in fact:
        ans.append(fact.index(na3))
        fact_copy.remove(na3)
        # print("I am in na3")
        continue

print_str = ""
for i in ans:
    print_str = print_str + str(series[i]) + " "

print(print_str.strip())