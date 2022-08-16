from pprint import pprint

# Finding the next empty area in the row or column
# That has not been filled out yet
# Used -1 as a indicator, to highlight a "blank" area on the grid.

def findNextEmpty(Puzzle):
    for r in range(9):
        for c in range(9):
            if Puzzle[r][c] ==  -1:
                return r, c

    return None, None

# Basically checks to make sure that the guess
# Is going to be a valid guess
# Making sure the guess follows the rules of suodku in the "3x3" grid.

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

# This uses backtracking to solve sudoku
# And this essentially returns wheter or not
# It can fine a solution using 
# True or False and then converts the grid to the solution if possible.

def sudokuSolver(Puzzle):
    row, col = findNextEmpty(Puzzle)            # Finds an empty area to make a guess.

    if row is None:                             # If there isnt any available rows we're done.
        return True                             
                                                # However if there is an empty space make a guess.
    for guess in range(1,10):                   # Takes a guess in the range of 1-10 (1-9) doesn't include 10.
        
        if isValid(Puzzle, guess, row, col):    # Checks if the proposed guess is valid or not.    
            Puzzle[row][col] = guess            # If the guess is valid, add it to the grid. 
            
            if sudokuSolver(Puzzle):            # Then call the function again and repeat the process. 
                return True
    
        Puzzle[row][col] = -1                   # If the previous statement doesn't return True, the guess wasn't valid.
                                                # So the code backtracks and takes a new guess.
                                                # If it can't make a succesful guess the puzzle is unsolvable. 
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


