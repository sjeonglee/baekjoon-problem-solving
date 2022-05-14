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

# get the starting number of the cross
sum_column = board.sum(axis = 0)
sum_row = board.sum(axis=1)
start_num = min(max(sum_column), max(sum_row))
# print(i)

if start_num % 2 != 1:
    start_num = start_num - 1

def get_cross_matrix(i:int, position:int):
    plain_board = np.zeros([N, M])
    for i in range(1, N + 1):
        for j in range(1, M + 1):




for i in range(N):
    for j in range(M):
