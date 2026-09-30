def solve_n_queens(n):
    """
    Finds all distinct solutions to the N-Queens problem.
    :param n: The size of the chessboard.
    :return: A list of all solutions, where each solution is a list of strings
             representing the board configuration.
    """
    solutions = []
    board = [['.' for _ in range(n)] for _ in range(n)]
    
    def is_safe(row, col):
        """
        Checks if placing a queen at board[row][col] is safe.
        """
        # Check the row and column
        for i in range(n):
            if board[row][i] == 'Q' or board[i][col] == 'Q':
                return False
        
        # Check diagonals
        for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
            if board[i][j] == 'Q':
                return False
        for i, j in zip(range(row, n, 1), range(col, -1, -1)):
            if board[i][j] == 'Q':
                return False
        for i, j in zip(range(row, -1, -1), range(col, n, 1)):
            if board[i][j] == 'Q':
                return False
        for i, j in zip(range(row, n, 1), range(col, n, 1)):
            if board[i][j] == 'Q':
                return False
        
        return True

        def backtrack(col):
            """
            Recursive function to place queens column by column.
            """
            if col == n:
                # All queens are placed, we've found a solution
                current_solution = [''.join(row) for row in board]
                solutions.append(current_solution)
                return

            for row in range(n):
                if is_safe(row, col):
                    board[row][col] = 'Q'
                    backtrack(col + 1)
                    # Backtrack: remove the queen to explore other possibilities
                    board[row][col] = '.'

    backtrack(0)
    return solutions

# --- Example Usage ---
n = 5# For a 4x4 board
solutions_list = solve_n_queens(n)

if solutions_list:
    print(f"Found {len(solutions_list)} solution(s) for N={n}:")
    for i, solution in enumerate(solutions_list):
        print(f"\nSolution {i + 1}:")
        for row in solution:
            print(row)
else:
    print(f"No solutions found for N={n}.")