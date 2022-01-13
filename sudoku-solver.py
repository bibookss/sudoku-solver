ARRAY = [ 
    [0, 0, 7, 5, 0, 0, 6, 0, 3], 
    [4, 3, 0, 0, 0, 6, 0, 0, 5], 
    [6, 0, 8, 1, 0, 9, 0, 2, 7], 
    [2, 0, 6, 4, 5, 0, 0, 0, 0], 
    [0, 0, 1, 0, 6, 0, 3, 4, 0], 
    [7, 0, 0, 0, 0, 8, 0, 5, 0], 
    [8, 0, 0, 7, 0, 0, 1, 3, 0], 
    [0, 7, 4, 0, 2, 0, 5, 9, 0], 
    [1, 0, 9, 3, 0, 5, 0, 0, 0] ]


def emptyCell(puzzle):
    for row in range(9):
        for col in range(9):
            if puzzle[row][col] == 0:
                return row, col
    return None, None

def isValid(row, col, puzzle, guess):
    # Check row
    for c in range(9):
        if puzzle[row][c] == guess:
            return False
    
    # Check col
    for r in range(9):
        if puzzle[r][col] == guess:
            return False
        
    # Check 3 by 3 squares
    _row = (row//3) * 3
    _col = (col//3) * 3

    for r in range(_row, _row + 3):
        for c in range(_col, _col + 3):
            if puzzle[r][c] == guess:
                return False
    
    return True

def printArray(puzzle):
    for r in range(9):
        print(puzzle[r])

def solvePuzzle(puzzle):
    # Find all empty cells
    row, col = emptyCell(puzzle)

    if row is None:
        return True

    # Make a guess from 1 to 9 (inclusive)
    for guess in range(1, 10):
        if isValid(row, col, puzzle, guess):
            puzzle[row][col] = guess
            # Solve again
            if solvePuzzle(puzzle):
                return True
        puzzle[row][col] = 0

    return False

def main():
    printArray(ARRAY)
    
main()
