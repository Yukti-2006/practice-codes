# sudoku_generator.py
import random
import copy
import sys

SIZE = 9
BOX = 3

def print_board(board):
    for r in range(SIZE):
        if r % BOX == 0 and r != 0:
            print("-" * (SIZE * 2 + BOX - 1))
        for c in range(SIZE):
            if c % BOX == 0 and c != 0:
                print("|", end=" ")
            val = board[r][c]
            print(val if val != 0 else ".", end=" ")
        print()
    print()

def possible(board, row, col, num):
    # Check row and column
    for i in range(SIZE):
        if board[row][i] == num: return False
        if board[i][col] == num: return False
    # Check box
    box_row = (row // BOX) * BOX
    box_col = (col // BOX) * BOX
    for r in range(box_row, box_row + BOX):
        for c in range(box_col, box_col + BOX):
            if board[r][c] == num:
                return False
    return True

def find_empty(board):
    for r in range(SIZE):
        for c in range(SIZE):
            if board[r][c] == 0:
                return (r, c)
    return None

def solve_backtrack(board):
    """Standard backtracking solver (fills board). Returns True if solved."""
    empty = find_empty(board)
    if not empty:
        return True
    r, c = empty
    for num in range(1, SIZE + 1):
        if possible(board, r, c, num):
            board[r][c] = num
            if solve_backtrack(board):
                return True
            board[r][c] = 0
    return False

def count_solutions(board, limit=2):
    """
    Count number of solutions up to `limit`. Uses backtracking.
    Early exit when count >= limit for speed.
    """
    # find empty
    empty = find_empty(board)
    if not empty:
        return 1
    r, c = empty
    count = 0
    for num in range(1, SIZE + 1):
        if possible(board, r, c, num):
            board[r][c] = num
            csub = count_solutions(board, limit)
            count += csub
            board[r][c] = 0
            if count >= limit:
                break
    return count

def fill_board_random(board):
    """Fill board completely with a valid Sudoku using randomized backtracking."""
    empty = find_empty(board)
    if not empty:
        return True
    r, c = empty
    numbers = list(range(1, SIZE + 1))
    random.shuffle(numbers)
    for num in numbers:
        if possible(board, r, c, num):
            board[r][c] = num
            if fill_board_random(board):
                return True
            board[r][c] = 0
    return False

def generate_full_solution():
    board = [[0] * SIZE for _ in range(SIZE)]
    fill_board_random(board)
    return board

def make_puzzle_from_solution(solution, holes=40, ensure_unique=True):
    """
    Remove `holes` cells from `solution` to create a puzzle.
    If ensure_unique=True, tries to keep puzzle with unique solution.
    """
    puzzle = copy.deepcopy(solution)
    cells = [(r, c) for r in range(SIZE) for c in range(SIZE)]
    random.shuffle(cells)

    removed = 0
    for (r, c) in cells:
        if removed >= holes:
            break
        backup = puzzle[r][c]
        puzzle[r][c] = 0

        if ensure_unique:
            # Check solutions count; use a copy because solver mutates board
            copy_board = copy.deepcopy(puzzle)
            sols = count_solutions(copy_board, limit=2)
            if sols != 1:
                # Revert removal if uniqueness breaks
                puzzle[r][c] = backup
                continue

        removed += 1

    return puzzle

def main(holes=40, ensure_unique=True, show_solution=False):
    print("Generating full Sudoku solution...")
    solution = generate_full_solution()
    print("Full solution:")
    print_board(solution)

    print(f"Removing {holes} cells to make puzzle (unique required={ensure_unique})...")
    puzzle = make_puzzle_from_solution(solution, holes=holes, ensure_unique=ensure_unique)
    print("Puzzle:")
    print_board(puzzle)

    if show_solution:
        print("Solution (for reference):")
        print_board(solution)

if __name__ == "__main__":
    # Basic CLI: python sudoku_generator.py [holes] [unique:0/1] [show_solution:0/1]
    holes = 40
    ensure_unique = True
    show_solution = False
    if len(sys.argv) > 1:
        try:
            holes = int(sys.argv[1])
        except:
            pass
    if len(sys.argv) > 2:
        ensure_unique = bool(int(sys.argv[2]))
    if len(sys.argv) > 3:
        show_solution = bool(int(sys.argv[3]))

    main(holes=holes, ensure_unique=ensure_unique, show_solution=show_solution)
