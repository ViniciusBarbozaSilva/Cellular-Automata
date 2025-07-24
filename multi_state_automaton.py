import random
import os
import time

WIDTH = 20
HEIGHT = 20
MAX_STATE = 2
THRESHOLD = 6
GENERATIONS = 50

def create_board():
    return [[random.randint(0, MAX_STATE) for _ in range(WIDTH)] for _ in range(HEIGHT)]

def count_neighbors(board, x, y):
    total = 0
    for dx in [-1,0,1]:
        for dy in [-1,0,1]:
            if dx == 0 and dy == 0:
                continue
            nx, ny = x+dx, y+dy
            if 0 <= nx < HEIGHT and 0 <= ny < WIDTH:
                total += board[nx][ny]
    return total

def next_generation(board):
    new_board = [[0]*WIDTH for _ in range(HEIGHT)]
    for x in range(HEIGHT):
        for y in range(WIDTH):
            neighbors = count_neighbors(board, x, y)
            if neighbors >= THRESHOLD:
                new_board[x][y] = (board[x][y]+1) % (MAX_STATE+1)
            else:
                new_board[x][y] = board[x][y]
    return new_board

def print_board(board):
    os.system('cls' if os.name == 'nt' else 'clear')
    symbols = [' ', '.', '*']
    for row in board:
        print(''.join([symbols[cell] for cell in row]))

def main():
    board = create_board()
    for _ in range(GENERATIONS):
        print_board(board)
        board = next_generation(board)
        time.sleep(0.2)

if __name__ == "__main__":
    main()
