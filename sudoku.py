#!/usr/bin/env python
#coding:utf-8

"""
Each sudoku board is represented as a dictionary with string keys and
int values.
e.g. my_board['A1'] = 8
"""
import sys
import time


ROW = "ABCDEFGHI"
COL = "123456789"


def print_board(board):
    """Helper function to print board in a square."""
    print("-----------------")
    for i in ROW:
        row = ''
        for j in COL:
            row += (str(board[i + j]) + " ")
        print(row)


def board_to_string(board):
    """Helper function to convert board dictionary to string for writing."""
    ordered_vals = []
    for r in ROW:
        for c in COL:
            ordered_vals.append(str(board[r + c]))
    return ''.join(ordered_vals)


def find_empty(board):
    for r in range(0, len(ROW)):
        for c in range(0, len(COL)):
            loc = str(ROW[r] + COL[c])
            if board[loc] == 0:
                return r, c
    return None, None

def is_valid(board, guess, row, col):
    #check box validity
    row_start = (row // 3) * 3
    col_start = (col // 3) * 3  
    for r in range (row_start, row_start+3):
        for c in range (col_start, col_start+3):
            loc = str(ROW[r] + COL[c])
            if board[loc] == guess:
                return False
    
    #row validity check
    for c in range(0, len(COL)):
        loc = str(ROW[row] + COL[c])
        if guess == board[loc]:
            return False

    #check for column validity
    for r in range(0, len(ROW)):
        loc = str(ROW[r] + COL[col])
        if guess == board[loc]:
            return False

    return True


def backtracking(board):
    """Takes a board and returns solved board."""
    # TODO: implement this
    row, col = find_empty(board)
    if row is None:
        return board

    loc = str(ROW[row] + COL[col])
    for guess in range (1, 10):
        if is_valid (board, guess, row, col):
            board[loc] = guess
            if backtracking(board):
                return board
        board[loc] = 0
    return None


if __name__ == '__main__':
    if len(sys.argv) > 1:
        
        # Running sudoku solver with one board $python3 sudoku.py <input_string>.
        print(sys.argv[1])
        # Parse boards to dict representation, scanning board L to R, Up to Down
        board = { ROW[r] + COL[c]: int(sys.argv[1][9*r+c])
                  for r in range(9) for c in range(9)}       
        
        solved_board = backtracking(board)
        # Write board to file
        out_filename = 'output.txt'
        outfile = open(out_filename, "w")
        outfile.write(board_to_string(solved_board))
        outfile.write('\n')

    else:
        # Running sudoku solver for boards in sudokus_start.txt $python3 sudoku.py

        #  Read boards from source.
        src_filename = 'sudokus_start.txt'
        try:
            srcfile = open(src_filename, "r")
            sudoku_list = srcfile.read()
        except:
            print("Error reading the sudoku file %s" % src_filename)
            exit()

        # Setup output file
        out_filename = 'output.txt'
        outfile = open(out_filename, "w")

        #Stats collector!
        #stat_filename = 'stats.txt'
        #stats = open(stat_filename, "w")

        # Solve each board using backtracking
        for line in sudoku_list.split("\n"):

            if len(line) < 9:
                continue

            # Parse boards to dict representation, scanning board L to R, Up to Down
            board = { ROW[r] + COL[c]: int(line[9*r+c])
                      for r in range(9) for c in range(9)}

            start = time.time()
            # Solve with backtracking
            solved_board = backtracking(board)
            end = time.time()
            elapsed = end - start
            #stats.write(str(elapsed))
            #stats.write('\n')
            # Write board to file
            outfile.write(board_to_string(solved_board))
            outfile.write('\n')




        print("Finishing all boards in file.")