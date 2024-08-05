import PySimpleGUI as sg  # Importing the PySimpleGUI library for pop-up dialogs
import random  # Importing the random library for generating random numbers
import pygame  # Importing the pygame library for creating the GUI

# Initializing pygame modules
pygame.init()
pygame.font.init()

# Defining color constants
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 255, 0)
GREEN = (0, 0, 255)
YELLOW = (255, 255, 0)
ORANGE = (255, 165, 0)
PURPLE = (138, 43, 226)
PINK = (255, 105, 180)
WEIRD_BLUE = (46, 80, 144)
GREY = (202, 193, 180)
BROWN = (133, 70, 30)
BLOOD_RED = (102, 0, 0)
VIRIDIAN = (64, 130, 109)

# Setting the font for the pop-up dialogs
font = ('Arial', 14)

# Setting the frames per second for the game loop
FPS = 240

# Setting the width and height of the window
WIDTH, HEIGHT = 600, 700

# Setting the number of rows and columns for the grid
ROWS = COLS = x

# Setting the height of the toolbar
TOOLBAR_HEIGHT = HEIGHT - WIDTH

# Setting the size of each pixel in the grid
PIXEL_SIZE = WIDTH // COLS

# Setting the background color of the window
BG_COLOR = WHITE

# Flag to indicate whether to draw grid lines
DRAW_GRID_LINES = True

# Initial brush size and number of undo steps
brush_size = 1
number_of_undos = 3

# Function to get the font for drawing text on buttons
def get_font(size):
    return pygame.font.SysFont("Times new roman", size)

# Class representing a button in the GUI
class Button:
    def __init__(self, x, y, width, height, color, text=None, text_color=BLACK):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.text = text
        self.text_color = text_color

    def draw(self, win):
        # Drawing the button
        pygame.draw.rect(win, self.color, (self.x, self.y, self.width, self.height))
        pygame.draw.rect(win, BLACK, (self.x, self.y, self.width, self.height), 2)
        if self.text:
            button_font = get_font(10)
            text_surface = button_font.render(self.text, 1, self.text_color)
            win.blit(text_surface, (self.x + self.width / 2 - text_surface.get_width()/2, self.y + self.height/2 - text_surface.get_height()/2))

    def clicked(self, pos):
        x, y = pos
        if not (x >= self.x and x <= self.x + self.width):
            return False
        if not (y >= self.y and y <= self.y + self.height):
            return False
        return True

# Setting up the pygame window
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("SDD MAJOR PROJECT")

# Function to initialize the grid with a specified color
def init_grid(rows, cols, color):
    grid = []
    for i in range(rows):
        grid.append([])
        for _ in range(cols):
            grid[i].append(color)
    return grid

# Function to draw the grid on the window
def draw_grid(win, grid, drawRows=True, drawCols=True):
    for i, row in enumerate(grid):
        for j, pixel in enumerate(row):
            pygame.draw.rect(win, pixel, (j * PIXEL_SIZE, i * PIXEL_SIZE, PIXEL_SIZE, PIXEL_SIZE))

    if drawRows:    
        if DRAW_GRID_LINES:
            for i in range(ROWS + 1):
                pygame.draw.line(win, BLACK, (0, i * PIXEL_SIZE), (WIDTH, i * PIXEL_SIZE))
            if drawCols:
                for i in range(COLS + 1):
                    pygame.draw.line(win, BLACK, (i * PIXEL_SIZE, 0), (i * PIXEL_SIZE, HEIGHT - TOOLBAR_HEIGHT))

# Function to draw the entire window including the grid and buttons
def draw(win, grid, buttons, drawRows=True, drawCols=True, drawButtons=True):
    win.fill(BG_COLOR)
    draw_grid(win, grid, drawRows, drawCols)
    if drawButtons:
        for button in buttons:
            button.draw(win)
    pygame.display.update()

# Function to get the row and column from the mouse position
def get_row_col_from_pos(pos):
    x, y = pos
    row = y // PIXEL_SIZE
    col = x // PIXEL_SIZE
    if row >= ROWS:
        raise IndexError
    return [row, col]

# Function to update the grid with the drawing color and brush size
def update_grid(_row, _col):
    grid[_row][_col] = drawing_color
    increment = brush_size // 2
    back_row = _row - increment
    front_row = _row + increment
    back_col = _col - increment
    front_col = _col + increment
    if back_row < 0:
        back_row = 0
    if back_col < 0:
        back_col = 0
    for row_no in range(back_row, front_row + 1):
        for col_no in range(back_col, front_col + 1):
            try:
                grid[row_no][col_no] = drawing_color
            except:
                continue

# Main game loop
run = True
clock = pygame.time.Clock()
grid = init_grid(ROWS, COLS, BG_COLOR)
drawing_color = BLACK

# Setting the positions of the buttons
button_y = HEIGHT - TOOLBAR_HEIGHT/2 - 25
button_y2 = button_y + 40  
buttons = [
    Button(10, button_y, 25, 25, BLACK),
    Button(10, button_y2, 25, 25, WEIRD_BLUE),
    Button(70, button_y, 25, 25, RED),
    Button(70, button_y2, 25, 25, GREY),
    Button(130, button_y, 25, 25, GREEN),
    Button(130, button_y2, 25, 25, BROWN),
    Button(190, button_y, 25, 25, BLUE),
    Button(190, button_y2, 25, 25, BLOOD_RED),
    Button(250, button_y, 25, 25, YELLOW),
    Button(250, button_y2, 25, 25, VIRIDIAN),
    Button(310, button_y, 25, 25, ORANGE),
    Button(370, button_y, 25, 25, PURPLE),
    Button(430, button_y, 25, 25, PINK),
    Button(430, button_y2, 30, 30, WHITE, 'S1', BLACK),
    Button(470, button_y, 30, 30, WHITE, "Erase", BLACK),
    Button(470, button_y2, 30, 30, WHITE, 'S2', BLACK),
    Button(520, button_y, 30, 30, WHITE, "Clear", BLACK),
    Button(520, button_y2, 30, 30, WHITE, 'S3', BLACK),
    Button(560, button_y, 30, 30, WHITE, "Undo", BLACK),
    Button(560, button_y2, 30, 30, WHITE, 'Save', BLACK)
]

# List to keep track of grid states for undo functionality
lastClicked = False
lastGrids = []

# Game loop
while run:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        if pygame.mouse.get_pressed()[0]:
            pos = pygame.mouse.get_pos()
            try:
                row, col = get_row_col_from_pos(pos)
                grid[row][col]
                if not lastClicked:
                    lastGrid = []
                    for index in grid:
                        lastGrid.append(index[:])
                    lastGrids.append(lastGrid)
                    if len(lastGrids) > number_of_undos:
                        lastGrids.pop(0)
                    lastClicked = True
                update_grid(row, col)
            except IndexError:
                for button in buttons:
                    if not button.clicked(pos):
                        continue
                    if button.text == "Clear":
                        grid = init_grid(ROWS, COLS, BG_COLOR)
                        drawing_color = BLACK
                    elif button.text == 'S1':
                        brush_size = 1
                    elif button.text == 'S2':
                        brush_size = 3
                    elif button.text == 'S3':
                        brush_size = 5
                    elif button.text == 'Save':
                        draw(WIN, grid, buttons, False, False, False)
                        save_file = 'screenshots' + str(random.randint(1, 10000000)) + '.png'
                        pygame.image.save(WIN, save_file)
                        sg.popup("Picture is saved", title='Save Screen', font=font)
                    elif button.text == "Undo":
                        if len(lastGrids) >= 1:
                            grid = []
                            for index in lastGrids[-1]:
                                grid.append(index[:])
                            lastGrids.pop()
                    else:
                        drawing_color = button.color
        else:
            lastClicked = False
    draw(WIN, grid, buttons)

pygame.quit()
