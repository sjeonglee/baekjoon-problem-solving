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

def get_cross_matrix(cross_size:int, middle_position:list): # middle_position = [row, column]
    plain_board = np.zeros([N, M])
    if (middle_position[0] - cross_size < 0) or (middle_position[1] - cross_size < 0):
        return plain_board
    elif (middle_position[0] + cross_size >= M) or (middle_position[1] + cross_size >= N):
        return plain_board
    else:
        plain_board[middle_position[0], middle_position[1] - cross_size:middle_position[1] + cross_size] = 1
        plain_board[middle_position[0] - cross_size:middle_position[0] + cross_size, middle_position[1]] = 1
        return plain_board

get_cross_matrix(1, [2, 2])
# for i in range(N):
#     for j in range(M):
