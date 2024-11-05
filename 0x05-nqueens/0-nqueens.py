#!/usr/bin/python3
"""N Queens Problem - Solves the N Queens Puzzle using Backtracking"""
import sys

def print_board(board):
    """Print each solution as a list of [row, col] positions of queens."""
    solution = []
    for row, col in enumerate(board):
        solution.append([row, col])
    print(solution)

def is_position_safe(board, row, col):
    """Check if placing a queen at board[row] == col is safe."""
    for i in range(row):
        if board[i] == col or \
           board[i] - i == col - row or \
           board[i] + i == col + row:
            return False
    return True

def solve_nqueens(board, row, n):
    """Recursive function to solve N Queens puzzle using backtracking."""
    if row == n:
        print_board(board)
    else:
        for col in range(n):
            if is_position_safe(board, row, col):
                board[row] = col
                solve_nqueens(board, row + 1, n)
                board[row] = -1  # Reset row after backtracking

if len(sys.argv) != 2:
    print("Usage: nqueens N")
    exit(1)

try:
    n = int(sys.argv[1])
except ValueError:
    print("N must be a number")
    exit(1)

if n < 4:
    print("N must be at least 4")
    exit(1)

board = [-1] * n  # Initialize the board with -1 (no queens placed yet)
solve_nqueens(board, 0, n)

