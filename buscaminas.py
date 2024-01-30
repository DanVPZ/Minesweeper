import random, pygame, sys, time

# Configura las variables indispensables para la ventana.
pygame.init()
clock = pygame.time.Clock()
screen_width = 700
screen_height = 700
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Minesweeper")

# Colores
grey = 230, 230, 230
green = 20, 100, 20
red = 255, 0, 0
black = 0, 0, 0

adjacent = 0

font = pygame.font.Font('freesansbold.ttf', 23)

screen.fill(green)

columns = 30 #int(input("Cuántas columnas quieres?\n>>>"))
rows = 30 #int(input("Cuántas columnas quieres?\n>>>"))
cell_size = screen_width / columns

# Crea el array de las celdas, con tantas filas y columnas como indicadas.
grid = []
for row in range(rows):
    grid.append([])
    for column in range(columns):
        grid[row].append(0)

mines = 99
for mine in range(mines):
    mine_row = random.randint(0, rows - 1)
    mine_column = random.randint(0, columns - 1)
    try:
        grid[mine_row][mine_column] = 1
        # pygame.draw.rect(screen, red, (mine_column * cell_size, mine_row * cell_size, cell_size, cell_size))
        pygame.display.update()
    except:
        pass

# Dibuja la cuadricula.
def draw_grid():
    for row in range(rows):
        pygame.draw.line(screen, black, (0, row * cell_size), (columns * cell_size, row * cell_size))
    for column in range(columns):
        pygame.draw.line(screen, black, (column * cell_size, 0), (column * cell_size, rows * cell_size))


def left_click():
    global adjacent
    adjacent = 0
    mouse_x, mouse_y = pygame.mouse.get_pos()
    row = int(mouse_y // cell_size)
    column = int(mouse_x // cell_size)
    if grid[row][column] == 1:
        pygame.draw.rect(screen, red, (column * cell_size, row * cell_size, cell_size, cell_size))
        pygame.display.update()
        # pygame.time.delay(7000)
        # pygame.quit()
        # sys.exit()
    else:
        pygame.draw.rect(screen, grey, (column * cell_size, row * cell_size, cell_size, cell_size))
        grid[row][column] = 80
        for i in range(-1, 2, 2):
            if grid[row][column - i] == 1:                
                adjacent += 1
                
            elif grid[row - i][column] == 1:
                adjacent += 1
                
        for i in range(-1, 2, 2):
            pos = grid[row + i][column + i] 
            pos2 = grid[row - i][column + i]      
            
            if pos == 1:
                adjacent += 1
            elif pos2 == 1:
                adjacent += 1
        number = font.render(f" {adjacent}", True, black)
        screen.blit(number,(column * cell_size, row * cell_size + 2))
        pygame.display.update()
        
def right_click():
    mouse_x, mouse_y = pygame.mouse.get_pos()
    row = mouse_y // cell_size
    column = mouse_x // cell_size
    pygame.draw.rect(screen, red, (column * cell_size + cell_size / 3.2, row * cell_size + cell_size / 3.2, (cell_size - cell_size / 2), (cell_size - cell_size / 2)))

# Main Loop
while True:
    for event in pygame.event.get():
        # Comprueba si se cierra el programa.
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        # Comprueba si se pulsa el ratón. 
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1: # 1 == left button
                left_click()
            elif event.button == 3:
                right_click()
    
    # Main functions are called.
    
    draw_grid()

    pygame.display.flip()
    clock.tick(60)