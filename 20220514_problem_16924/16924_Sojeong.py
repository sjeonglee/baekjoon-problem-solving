import numpy as np

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
# print(board)
board = np.array(board)
# print(board)

# get the starting number of the cross. start_num is the number of stars (not size)
sum_column = board.sum(axis = 0)
sum_row = board.sum(axis=1)
start_num = min(max(sum_column), max(sum_row))
# print(i)

if start_num % 2 != 1:
    start_num = start_num - 1

# cross의 size와 position에 따라 cross matrix를 냄
def get_cross_matrix(cross_size:int, middle_position:list): # middle_position = [row, column]
    plain_board = np.zeros([N, M])
    if (middle_position[0] - cross_size < 0) or (middle_position[1] - cross_size < 0):
        return plain_board
    elif (middle_position[0] + cross_size >= M) or (middle_position[1] + cross_size >= N):
        return plain_board
    else:
        plain_board[middle_position[0], middle_position[1] - cross_size:middle_position[1] + cross_size + 1] = 1
        plain_board[middle_position[0] - cross_size:middle_position[0] + cross_size + 1, middle_position[1]] = 1
        return plain_board


# for i in range(N):
#     for j in range(M):
#         if board[i, j] == 1:
# 모든 좌표들에 대해 점이 1이면 해당 점을 중심으로 십자가를 그려서 빼본다
# (board copy에서 빼기. 가장 큰 것부터 차례로. board copy에서 빼고, 음수가 없으면 해당 부분을
# board에서 빼서 보관. 전부 0보다 작을 때 성공해서 답을 쓰기.)