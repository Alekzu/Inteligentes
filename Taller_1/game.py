# import pygame library
import pygame
# initialise the pygame font
pygame.font.init()
# Total window
screen = pygame.display.set_mode((500, 600))
# Title and Icon
pygame.display.set_caption("Seppukus")
#img = pygame.image.load('icon.png')
#pygame.display.set_icon(img)

#test boards
grid1 = [
    [7, 8, 0, 4, 0, 0, 1, 2, 0],
    [6, 0, 0, 0, 7, 5, 0, 0, 9],
    [0, 0, 0, 6, 0, 1, 0, 7, 8],
    [0, 0, 7, 0, 4, 0, 2, 6, 0],
    [0, 0, 1, 0, 5, 0, 9, 3, 0],
    [9, 0, 4, 0, 6, 0, 0, 0, 5],
    [0, 7, 0, 3, 0, 0, 0, 1, 2],
    [1, 2, 0, 0, 0, 7, 4, 0, 0],
    [0, 4, 9, 2, 0, 6, 0, 0, 7]
]
#solved board
resp1 = [
        [7, 8, 5, 4, 3, 9, 1, 2, 6],
        [6, 1, 2, 8, 7, 5, 3, 4, 9],
        [4, 9, 3, 6, 2, 1, 5, 7, 8],
        [8, 5, 7, 9, 4, 3, 2, 6, 1],
        [2, 6, 1, 7, 5, 8, 9, 3, 4],
        [9, 3, 4, 1, 6, 2, 7, 8, 5],
        [5, 7, 8, 3, 9, 4, 6, 1, 2],
        [1, 2, 6, 5, 8, 7, 4, 9, 3],
        [3, 4, 9, 2, 1, 6, 8, 5, 7]
    ]
# Default Sudoku Boards.
#initial
grid = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0]
        ]
#full (solved)
resp = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0]
        ]

# Load test fonts for future use
font1 = pygame.font.SysFont("comicsans", 40)
font2 = pygame.font.SysFont("comicsans", 20)

# Highlight the cell selected
def draw_box(x,y):
    dif = 500 / 9
    for i in range(2):
        pygame.draw.line(screen, (255, 0, 0), (x * dif - 3, (y + i) * dif), (x * dif + dif + 3, (y + i) * dif), 7)
        pygame.draw.line(screen, (255, 0, 0), ((x + i) * dif, y * dif), ((x + i) * dif, y * dif + dif), 7)

# Function to draw required lines for making Sudoku grid
def draw(board):
    dif = 500 / 9
    # Draw the lines

    for i in range(9):
        for j in range(9):
            if board[i][j] != 0:
                # Fill blue color in already numbered grid
                pygame.draw.rect(screen, (0, 153, 153), (i * dif, j * dif, dif + 1, dif + 1))
                # Fill gird with default numbers specified changed
                text1 = font1.render(str(board[i][j]), 1, (0, 0, 0))
                screen.blit(text1, (i * dif + 15, j * dif + 15))
                # Draw lines horizontally and verticallyto form grid
    for i in range(10):
        if i % 3 == 0:
            thick = 7
        else:
            thick = 1
        pygame.draw.line(screen, (0, 0, 0), (0, i * dif), (500, i * dif), thick)
        pygame.draw.line(screen, (0, 0, 0), (i * dif, 0), (i * dif, 500), thick)

# Solves the sudoku board like a pro
def solve(board, solved):
    dig = 1
    pygame.event.pump()
    while dig < 10:
        for i in range(0, 9):
            for j in range(0, 9):
                if solved[i][j] == dig:
                    board[i][j] = dig
                    screen.fill((255, 255, 255))
                    draw(board)
                    draw_box(i,j)
                    pygame.display.update()
                    pygame.time.delay(150)
        dig = dig + 1
    return True

# Display instruction for the game
def instruction():
    text1 = font2.render("PRESS ENTER TO SOLVE", 1, (0, 0, 0))
    screen.blit(text1, (20, 520))

# Display options when solved
def result():
    text1 = font1.render("FINISHED", 1, (0, 0, 0))
    screen.blit(text1, (20, 570))
#Intialize boards
def setBoards(board1, board2):
    global grid,resp
    grid = board1
    resp = board2
#boards to draw
setBoards(grid1,resp1)
run = True
flag2 = 0
error = 0
# The loop that keeps the window running
while run:

    # White color background
    screen.fill((255, 255, 255))
    # Loop through the events stored in event.get()
    for event in pygame.event.get():
        # Quit the game window
        if event.type == pygame.QUIT:
            run = False
            # Get the mouse postion to insert number
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                flag2 = 1

    if flag2 == 1:
        if solve(grid, resp) == False:
            error = 1
        else:
            result()
        flag2 = 0
    draw(grid)
    instruction()

    # Update window
    pygame.display.update()

# Quit pygame window
pygame.quit()
