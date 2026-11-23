"""matrix: given matrix to build a conways game of life"""

def tick(matrix):
    """matrix: given matrix to build a conways game of life"""
    # Handle an empty matrix edge case
    if not matrix or not matrix[0]:
        return []

    rows = len(matrix)
    cols = len(matrix[0])
    
    # Create a new matrix initialized with 0s for the next generation
    next_gen = [[0] * cols for _ in range(rows)]

    # Iterate over every cell in the grid
    for row in range(rows):
        for c in range(cols):
            live_neighbors = 0
            
            # Check all 8 adjacent neighbors
            for difference_row in (-1, 0, 1):
                for difference_column in (-1, 0, 1):
                    # Skip the cell itself
                    if difference_row == 0 and difference_column == 0:
                        continue
                    
                    nr, nc = row + difference_row, c + difference_column
                    
                    # Ensure the neighbor is within grid boundaries
                    if 0 <= nr < rows and 0 <= nc < cols:
                        live_neighbors += matrix[nr][nc]

            # Apply Conway's rules
            if matrix[row][c] == 1 and live_neighbors in (2, 3):
                next_gen[row][c] = 1
            elif matrix[row][c] == 0 and live_neighbors == 3:
                next_gen[row][c] = 1

    return next_gen
