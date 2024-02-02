import pygame
import os

# Initialize Pygame
pygame.init()

# Define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (150, 150, 150)

# Set the width and height of the screen [width, height]
SCREEN_SIZE = (400, 400)
screen = pygame.display.set_mode(SCREEN_SIZE)

# Set the title of the window
pygame.display.set_caption("8 Queens Problem")

# Define font for messages
font = pygame.font.Font(None, 36)

# Load queen image
queen_img = pygame.image.load("queen-chess-king-computer-icons-queen.jpg")
queen_img = pygame.transform.scale(queen_img, (SCREEN_SIZE[0] // 8, SCREEN_SIZE[1] // 8))

# Define the paths to the prize pictures
loseprize = "C:/Tài liệu đại học/AI/loseprize.jpeg"
winprize = "C:/Tài liệu đại học/AI/winprize.jpg"

# Load the prize pictures
lose_prize_img = pygame.image.load(loseprize)
lose_prize_img = pygame.transform.scale(lose_prize_img, SCREEN_SIZE)
win_prize_img = pygame.image.load(winprize)
win_prize_img = pygame.transform.scale(win_prize_img, SCREEN_SIZE)


# Load wrong_moves image
wrong_moves_img = pygame.image.load("wrong_moves.png")
wrong_moves_img = pygame.transform.scale(wrong_moves_img, (SCREEN_SIZE[0] // 8, SCREEN_SIZE[1] // 8))

def draw_board(board, wrong_moves=None):
    screen.fill(WHITE)
    cell_width = SCREEN_SIZE[0] // len(board)
    cell_height = SCREEN_SIZE[1] // len(board)
    for i in range(len(board)):
        for j in range(len(board[i])):
            color = WHITE if (i + j) % 2 == 0 else BLACK
            pygame.draw.rect(screen, color, [j * cell_width, i * cell_height, cell_width, cell_height])
            if board[i][j] == 1:
                # Blit queen image at the center of the cell
                queen_rect = queen_img.get_rect()
                queen_rect.center = (j * cell_width + cell_width // 2, i * cell_height + cell_height // 2)
                screen.blit(queen_img, queen_rect)
            elif wrong_moves and wrong_moves[0] == i and wrong_moves[1] == j:
                # Blit wrong_moves image at the center of the cell
                wrong_moves_rect = wrong_moves_img.get_rect()
                wrong_moves_rect.center = (j * cell_width + cell_width // 2, i * cell_height + cell_height // 2)
                screen.blit(wrong_moves_img, wrong_moves_rect)

def attack(i, j, board):
    # checking vertically and horizontally
    for k in range(0, 8):
        if board[i][k] == 1 or board[k][j] == 1:
            return True
    # checking diagonally
    for k in range(0, 8):
        for l in range(0, 8):
            if (k + l == i + j) or (k - l == i - j):
                if board[k][l] == 1:
                    return True
    return False

def N_queens(n, board):
    if n == 0:
        return True
    for i in range(0, 8):
        for j in range(0, 8):
            if (not attack(i, j, board)) and (board[i][j] != 1):
                board[i][j] = 1
                if N_queens(n - 1, board) == True:
                    return True
                board[i][j] = 0
    return False

def get_available_moves(queen_count, queens_positions):
    moves = []
    for i in range(1, 9):
        for j in range(1, 9):
            moves.append((i, j))
    for row, col in queens_positions:
        for i in range(1, 9):
            if (row, i) in moves:
                moves.remove((row, i))  # Remove moves in the same row
            if (i, col) in moves:
                moves.remove((i, col))  # Remove moves in the same column
            if (row - i, col - i) in moves:
                moves.remove((row - i, col - i))  # Remove moves in the same diagonal
            if (row + i, col + i) in moves:
                moves.remove((row + i, col + i))  # Remove moves in the same diagonal
            if (row + i, col - i) in moves:
                moves.remove((row + i, col - i))  # Remove moves in the same diagonal
            if (row - i, col + i) in moves:
                moves.remove((row - i, col + i))  # Remove moves in the same diagonal
    return moves

# Default 8x8 chessboard with no queens
board = [[0] * 8 for _ in range(8)]

# Main loop
running = True
queen_count = 0
queens_positions = []
wrong_moves = None

while running:
    available_moves = get_available_moves(queen_count, queens_positions)
    if not available_moves:
        running = False
    else:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                row = pos[1] // (SCREEN_SIZE[1] // 8)
                col = pos[0] // (SCREEN_SIZE[0] // 8)
                if (row + 1, col + 1) in available_moves:
                    board[row][col] = 1
                    queens_positions.append((row + 1, col + 1))
                    queen_count += 1
                    wrong_moves = None  # Clear wrong moves if a valid move is made
                else:
                    wrong_moves = (row, col)  # Set wrong moves coordinates

    # Draw the board
    draw_board(board, wrong_moves)
    
    # Update display
    pygame.display.flip()
# Screen 2
screen.fill(WHITE)

# Determine result message and prize picture
if queen_count == 8:
    result_message = "CONGRATULATIONS, YOU WIN!"
    prize_picture = winprize
else:
    result_message = "GAME OVER! YOU LOSE"
    prize_picture = loseprize

# Load prize picture
prize_img = pygame.image.load(prize_picture)
prize_img = pygame.transform.scale(prize_img, SCREEN_SIZE)

# Blit prize picture
screen.blit(prize_img, (0, 0))

# Render and blit result message
message_surface = font.render(result_message, True, BLACK)
message_rect = message_surface.get_rect(center=(SCREEN_SIZE[0] // 2, SCREEN_SIZE[1] - 50))
screen.blit(message_surface, message_rect)

# Update display
pygame.display.flip()

# Screen 2 event loop
screen2_active = True
while screen2_active:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            screen2_active = False

# Quit Pygame
pygame.quit()
