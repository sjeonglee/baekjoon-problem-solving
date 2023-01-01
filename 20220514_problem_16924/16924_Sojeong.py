# import numpy as np

N, M = map(int, input().strip().split())
# print(N)
# print(M)

# get the board
board = []
for i in range(N):
    temp = input()
    temp_row = []
    for j in range(M):
        if temp[j] == ".":
            temp_row.append(0)
        else:
            temp_row.append(1)
    board.append(temp_row)
print(board)
# board = np.array(board)
# print(board)

# # get the starting number of the cross. start_num is the number of stars (not size)
# sum_column = board.sum(axis = 0)
# sum_row = board.sum(axis=1)
# start_num = min(max(sum_column), max(sum_row))
# # print(i)

start_num = min(N, M)
if start_num % 2 != 1:
    start_num = start_num - 1

# cross의 size와 position에 따라 cross matrix를 냄
def get_cross_matrix(cross_size:int, middle_position:list): # middle_position = [row, column]
    plain_board = []
    for a in range(N):
        line = []
        for b in range(M):
            line.append(0)
        plain_board.append(line)
    # plain_board = np.zeros([N, M])

    if (middle_position[0] - cross_size < 0) or (middle_position[1] - cross_size < 0):
        return plain_board
    elif (middle_position[0] + cross_size >= N) or (middle_position[1] + cross_size >= M):
        return plain_board
    else:
        plain_board[middle_position[0], middle_position[1] - cross_size:middle_position[1] + cross_size + 1] = 1
        plain_board[middle_position[0] - cross_size:middle_position[0] + cross_size + 1, middle_position[1]] = 1
        return plain_board

def minus_matrix(list1:list, list2:list):
    answer = []
    for a in range(N):
        line = []
        for b in range(M):
            line.append(list1[a][b] - list2[a][b])
        answer.append(line)
    return answer

boardcopy = board.copy()
current_cross = start_num
crosses = []
for i in range(N):
    for j in range(M):

        # 만일 십자가의 가능성이 있다면
        if board[i][j] == 1:
            cross_num = start_num // 2

            while cross_num > 0:
                cross = get_cross_matrix(cross_num, [i, j])

                # 만일 십자가가 안그려지면, 십자가를 작게 해서 재도전
                if max(cross) == 0:
                    cross_num = cross_num - 1
                    continue

                # 만일 십자가가 그려지면, 십자가를 빼본다
                tempboard = minus_matrix(board, cross)

                # 십자가 빼기가 안 될 경우에는, 십자가를 작게 해서 재도전
                if (tempboard < 0).sum() > 0:
                    cross_num = cross_num - 1
                    continue
                else:  # 만일 십자가 빼기가 된다면
                    crosses.append([i+1, j+1, cross_num]) # 십자가 기록
                    boardcopy = minus_matrix(boardcopy, cross)         # 십자가 뺀 것도 기록
                    # print("The cross is")
                    # print(crosses)
                    # print("After minus cross is")
                    # print(boardcopy)
                    break

if (boardcopy > 0).sum() > 0:
    print("-1")
else:
    print(len(crosses))
    for c in crosses:
        print('{0} {1} {2}'.format(c[0], c[1], c[2]))


# 모든 좌표들에 대해 점이 1이면 해당 점을 중심으로 십자가를 그려서 빼본다
# (board copy에서 빼기. 가장 큰 것부터 차례로. board copy에서 빼고, 음수가 없으면 해당 부분을
# board에서 빼서 보관. 전부 0보다 작을 때 성공해서 답을 쓰기.)
