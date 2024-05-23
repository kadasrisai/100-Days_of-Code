class Solution(object):
    def solveSudoku(self, board):
        # Start solving Sudoku from the first cell
        self.solve(board, 0, 0)

    def solve(self, board, row, col):
        # Base case: If row is equal to board length, entire board has been filled
        if row == len(board):
            return True
        
        # Move to next row when current row is fully filled
        if col == len(board[0]):
            return self.solve(board, row + 1, 0)
        
        # Skip cells that are already filled
        if board[row][col] != '.':
            return self.solve(board, row, col + 1)
        
        # Try different numbers in the current cell
        for num in '123456789':
            if self.isValidPlacement(board, row, col, num):
                board[row][col] = num  # Fill current cell with valid number
                
                # Move to next cell
                if self.solve(board, row, col + 1):
                    return True
                
                # Backtrack to previous state if solution not found
                board[row][col] = '.'
        
        # No valid solution found
        return False

    def isValidPlacement(self, board, row, col, num):
        # Check if num is already in the same row, column, or 3x3 subgrid
        for i in range(len(board)):
            # Check row
            if board[row][i] == num:
                return False

            # Check column
            if board[i][col] == num:
                return False
            
            # Check 3x3 subgrid
            subgrid_row = 3 * (row // 3) + i // 3
            subgrid_col = 3 * (col // 3) + i % 3
            
            if board[subgrid_row][subgrid_col] == num:
                return False
        
        # Placement is valid
        return True
        
    
    
        