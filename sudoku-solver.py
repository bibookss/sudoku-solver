import pygame as py

BLOCK_SIZE = 100
WIDTH = 900
HEIGHT = 1000
ROWS = int(WIDTH/BLOCK_SIZE)
COLS = int(WIDTH/BLOCK_SIZE)
WHITE = (255, 255, 255)
BLACK = (0, 0 , 0)
RED = (255, 0, 0)
SILVER = (192, 192, 192)
BLUE = (173, 216, 230)
FPS = 120

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
            displaySudoku(puzzle)
            if solvePuzzle(puzzle):
                return True
        puzzle[row][col] = 0

    return False

def drawGrid():
    for x in range (0, WIDTH, BLOCK_SIZE):
        if x % 3 == 0:
            py.draw.line(gameDisplay, BLACK, (x, 0), (x, WIDTH), 2)
        else:
            py.draw.line(gameDisplay, SILVER, (x, 0), (x, WIDTH), 1)
    
    for y in range (0, WIDTH, BLOCK_SIZE):
        if y % 3 == 0:
            py.draw.line(gameDisplay, BLACK, (0, y), (WIDTH, y), 2)
        else:
            py.draw.line(gameDisplay, SILVER, (0, y), (WIDTH, y), 1)
    py.display.flip()

def displaySudoku(puzzle):
    for y in range(ROWS):
        for x in range(COLS):
            if puzzle[y][x] == 0:
                py.draw.rect(gameDisplay, BLUE, [x * BLOCK_SIZE, y * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE], 0)
                drawGrid()
            else:
                py.draw.rect(gameDisplay, WHITE, [x * BLOCK_SIZE, y * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE], 0)    
                py.draw.rect(gameDisplay, SILVER, [x * BLOCK_SIZE, y * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE], 1)
                number = py.font.SysFont("arial", BLOCK_SIZE).render(str(puzzle[y][x]), True, BLACK)
                gameDisplay.blit(number, [x * BLOCK_SIZE + 25, y * BLOCK_SIZE])
    py.display.flip()
    gameClock.tick(FPS)

            
def main():
    global gameDisplay, gameClock
    py.init()
    gameDisplay = py.display.set_mode([WIDTH, HEIGHT])
    gameClock = py.time.Clock()
    py.display.set_caption("Sudoku Solver")

    displaySudoku(ARRAY)

    simulationExit = False
    py.draw.rect(gameDisplay, WHITE, [0, 9 * BLOCK_SIZE, WIDTH, WIDTH], 0)

    while not simulationExit:
        for event in py.event.get():
            if event.type == py.QUIT:
               simulationExit = True
               exit()
            if event.type == py.KEYDOWN:
                if event.key == py.K_q:
                    simulationExit = True
                    exit()
                if event.key == py.K_c:
                    main()
        if solvePuzzle(ARRAY):
            solved = py.font.SysFont("arial", BLOCK_SIZE).render(("SOLVED!"), True, BLACK)
            gameDisplay.blit(solved, [3 * BLOCK_SIZE, 9 * BLOCK_SIZE])
        py.display.flip()
        gameClock.tick(FPS)

main()
