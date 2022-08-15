from pprint import pprint


def findNextEmpty(Puzzle):
    for r in range(9):
        for c in range(9):
            if Puzzle[r][c] ==  -1:
                return r, c

    return None, None

def isValid(Puzzle, guess, row, col):
    rowValues = Puzzle[row]
    if guess in rowValues:
        return False
    
    colValues = [Puzzle[i][col] for i in range(9)]
    if guess in colValues:
        return False

    rowStart = (row // 3) * 3
    colStart = (col // 3) * 3

    for r in range (rowStart, rowStart+3):
        for c in range(colStart, colStart+3):
            if Puzzle[r][c] == guess:
                return False
    return True



def sudokuSolver(Puzzle):
    row, col = findNextEmpty(Puzzle)

    if row is None:
        return True

    for guess in range(1,10): 
        if isValid(Puzzle, guess, row, col):
            Puzzle[row][col] = guess
            
            if sudokuSolver(Puzzle):
                return True
    
        Puzzle[row][col] = -1
    return False


if __name__ == '__main__':

    exampleBoard = [
    # [4, -1, 6,   -1, 7, -1,   9, -1, -1],
	# [9, -1, -1,   -1, -1, -1,   -1, 2, -1],
	# [-1, 3, -1,   -1, 2, -1,   1, 5, -1],

	# [-1, 8, -1,   2, 3, -1,   -1, 9, -1],
	# [5, 9, -1,   4, 6, -1,   8, -1, -1],
	# [1, -1, 3,   -1, 9, 8,   2, -1, 7],

	# [-1, 1, -1,   -1, 5, 9,   4, -1, 2],
	# [-1, 4, 5,   7, -1, -1,   -1, 8, 9],
	# [3, 7, -1,   -1, 4, -1,   5, -1, -1]
    
    [-1, -1, 6,   -1, -1, -1,   -1, -1, -1],
	[9, -1, -1,   -1, -1, -1,   -1, 2, -1],
	[-1, -1, -1,   -1, 2, -1,   1, 5, -1],

	[-1, -1, -1,   2, 3, -1,   -1, 9, -1],
	[-1, -1, -1,   -1, 6, -1,   -1, -1, -1],
	[1, -1, 3,   -1, 6, -1,   -1, -1, 7],

	[-1, -1, -1,   -1, -1, 9,   4, -1, 2],
	[-1, 4, 5,   7, -1, -1,   -1, 8, 9],
	[3, 7, -1,   -1, -1, -1,   5, -1, -1]
    ]
    print(sudokuSolver(exampleBoard))
    pprint(exampleBoard)



############################################################
# TEST BOARD - DOESN'T WORK.
############################################################
    
    # Disclaimer; this can't handle too complex games of sudoku 
    # And it's because it kinda break my recursion 
    # The original board I was testing on is below and the game can't
    # seem to process that particular board. 

    # [-1, -1, 6,   -1, -1, -1,   -1, -1, -1],
	# [9, -1, -1,   -1, -1, -1,   -1, 2, -1],
	# [-1, -1, -1,   -1, 2, -1,   1, 5, -1],

	# [-1, -1, -1,   2, 3, -1,   -1, 9, -1],
	# [-1, -1, -1,   -1, 6, -1,   -1, -1, -1],
	# [1, -1, 3,   -1, 6, -1,   -1, -1, 7],

	# [-1, -1, -1,   -1, -1, 9,   4, -1, 2],
	# [-1, 4, 5,   7, -1, -1,   -1, 8, 9],
	# [3, 7, -1,   -1, -1, -1,   5, -1, -1]

############################################################
# Couldn't find the level of complexity that breaks the code
# But that particular board does, so I filled it out a bit.
############################################################


