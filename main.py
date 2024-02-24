import pygame

pygame.init()

WIDTH = 600
HEIGHT = 600

board_width = 600
board_height = 600

screen = pygame.display.set_mode((WIDTH, HEIGHT))

white = (255, 255, 255)
black = (0, 0, 0)

row_cell_count = 30
col_cell_count = 30

board = [[0] * row_cell_count for i in range(col_cell_count)]


def draw_board():
    cell_size = board_width / row_cell_count
    for row in range(row_cell_count):
        for col in range(col_cell_count):
            cell_color = black if board[row][col] == 1 else white
            pygame.draw.rect(screen, cell_color, (col * cell_size, row * cell_size, cell_size, cell_size))
            pygame.draw.rect(screen, black, (col * cell_size, row * cell_size, cell_size, cell_size), 1)


def check_the_life_cell():
    cell_check = [(0, -1), (0, 1), (-1, -1), (-1, 0), (-1, 1), (1, -1), (1, 0), (1, 1)]
    for row in range(row_cell_count):
        for col in range(col_cell_count):
            live_cell = 0
            for cell in cell_check:
                if row + cell[0] < row_cell_count and col + cell[1] < col_cell_count:
                    if board[row + cell[0]][col + cell[1]] == 1:
                        live_cell += 1
                else:
                    check_row_cell = row + cell[0]
                    check_col_cell = col + cell[1]
                    if row + cell[0] == row_cell_count:
                        check_row_cell = 0
                    if col + cell[1] == col_cell_count:
                        check_col_cell = 0
                    if col + cell[1] == -1:
                        check_col_cell = col_cell_count - 1
                    if row + cell[0] == -1:
                        check_row_cell = row_cell_count - 1
                    if board[check_row_cell][check_col_cell] == 1:
                        live_cell += 1

            if board[row][col] == 1:
                if live_cell < 2 or live_cell > 3:
                    board[row][col] = 0
            else:
                if live_cell == 3:
                    board[row][col] = 1


running = True
start_game = False
fps = 10
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()

            cell_size = board_width // row_cell_count
            row = mouse_y // cell_size
            col = mouse_x // cell_size

            board[row][col] = 1 - board[row][col]

        if event.type == pygame.KEYDOWN or event.type == pygame.KEYUP:
            if event.key == pygame.K_s:
                start_game = True

            if event.key == pygame.K_f:
                start_game = False

            if event.key == pygame.K_RIGHT:
                fps += 5

            if event.key == pygame.K_LEFT:
                fps -= 1

    if start_game:
        check_the_life_cell()

    screen.fill(white)
    draw_board()
    pygame.display.flip()
    pygame.time.Clock().tick(fps)

pygame.quit()
