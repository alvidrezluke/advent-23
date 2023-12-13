file = open("./luke_input.txt")

board = []

def check_surroundings(row_index, col_index):
    for r in range(row_index - 1, row_index + 2):
        if r > 0 and r < len(board):
            for c in range (col_index - 1, col_index + 2):
                if c > 0 and c < len(board[r]):
                    if board[r][c] in "!@#$%^&*()-+?_=,<>/":
                        return True
                    
    return False


for line in file.readlines():
    board.append(line.strip())

sum = 0

############ PART 1 ############

# for [count, line] in enumerate(board):
#     line_iter = enumerate(line)
#     for [num, char] in line_iter:
#         if char.isnumeric():
#             start_num = num
#             end_num = num
#             total_num = char
#             still_num = True
#             while still_num:
#                 if end_num < len(line) - 1 and line[end_num + 1].isnumeric():
#                     [newnum, newchar] = line_iter.__next__()
#                     end_num = newnum
#                     total_num += newchar
#                 else:
#                     still_num = False

#             for i in range(start_num, end_num + 1):
#                 if check_surroundings(count, i):
#                     sum += int(total_num)
#                     break
            
# print(f"Sum: {sum}")

############ PART 2 ############
def find_full_number(row_index, col_index):
    for [num, _] in enumerate(board[row_index]):
        if num < col_index:
            length = 0
            for i in range(num, len(board[row_index])):
                if not board[row_index][i].isnumeric():
                    break
                else:
                    length += 1

    print(board[row_index][col_index:col_index + length - 1])



                    
for [count, line] in enumerate(board):
    for [num, char] in enumerate(line):
        if char == "*":
            find_full_number(count - 1, num - 1)
