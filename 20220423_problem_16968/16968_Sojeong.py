import sys

form = sys.stdin.readline().strip()

answer = 1
overlap_flag = False
right_before = None

for s in form:
    if right_before == s:
        overlap_flag = True
    if s == "c" and overlap_flag == False:
        answer = answer * 26
        right_before = "c"
    elif s == "c" and overlap_flag == True:
        answer = answer * 25
        right_before = "c"
    elif s == "d" and overlap_flag == False:
        answer = answer * 10
        right_before = "d"
    else:
        answer = answer * 9
        right_before = "d"

    overlap_flag = False

print(answer)