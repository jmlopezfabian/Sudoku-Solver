class SudokuSolver:
    def __init__(self, board):
        self.board = board

    def is_valid_board(self, row, column, num):
        for i in range(9):
            if self.board[row][i] == num or self.board[i][column] == num:
                return False

        start_row = (row // 3) * 3
        start_col = (column // 3) * 3
        for i in range(3):
            for j in range(3):
                if self.board[start_row + i][start_col + j] == num:
                    return False

        return True

    def find_empty_cell(self):
        for row in range(9):
            for col in range(9):
                if self.board[row][col] == 0:
                    return row, col
        return None, None

    def solve(self):
        row, col = self.find_empty_cell()

        if row is None and col is None:
            return True  # El Sudoku ya está resuelto

        for num in range(1, 10):
            if self.is_valid_board(row, col, num):
                self.board[row][col] = num
                # Llamada recursiva para continuar con la siguiente celda vacía
                if self.solve():
                    return True  # Sudoku resuelto
                self.board[row][col] = 0

        return False
