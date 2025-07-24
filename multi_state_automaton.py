import os
import time

WIDTH = 20
HEIGHT = 20
GENERATIONS = 50

HEALTHY = 0
INFECTED = 1
IMMUNE = 2
RECOVERING = 3
NUM_STATES = 4
INFECTION_THRESHOLD = 2

def create_board():
    board = [[HEALTHY for _ in range(WIDTH)] for _ in range(HEIGHT)]
    board[HEIGHT // 2][WIDTH // 2] = INFECTED
    return board

def count_infected_neighbors(board, x, y):
    infected = 0
    for dx in [-1, 0, 1]:
        for dy in [-1, 0, 1]:
            if dx == 0 and dy == 0:
                continue
            nx, ny = x + dx, y + dy
            if 0 <= nx < HEIGHT and 0 <= ny < WIDTH:
                if board[nx][ny] == INFECTED:
                    infected += 1
    return infected

def next_generation(board):
    new_board = [[HEALTHY for _ in range(WIDTH)] for _ in range(HEIGHT)]
    for x in range(HEIGHT):
        for y in range(WIDTH):
            state = board[x][y]
            infected_neighbors = count_infected_neighbors(board, x, y)

            if state == HEALTHY:
                if infected_neighbors >= INFECTION_THRESHOLD:
                    new_board[x][y] = INFECTED
                else:
                    new_board[x][y] = HEALTHY
            elif state == INFECTED:
                new_board[x][y] = IMMUNE
            elif state == IMMUNE:
                new_board[x][y] = RECOVERING
            elif state == RECOVERING:
                new_board[x][y] = HEALTHY
    return new_board

def print_board(board):
    os.system('cls' if os.name == 'nt' else 'clear')
    symbols = [' ', '*', 'o', '.']  # Saudável, Infectado, Imune, Recuperando
    for row in board:
        print(''.join(symbols[cell] for cell in row))

def main():
    board = create_board()
    for _ in range(GENERATIONS):
        print_board(board)
        board = next_generation(board)
        time.sleep(0.3)

if __name__ == "__main__":
    main()
