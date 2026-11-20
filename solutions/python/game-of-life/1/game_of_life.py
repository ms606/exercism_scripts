def tick(matrix):
    # Handle an empty matrix edge case
    if not matrix or not matrix[0]:
        return []

    rows = len(matrix)
    cols = len(matrix[0])
    
    # Create a new matrix initialized with 0s for the next generation
    next_gen = [[0] * cols for _ in range(rows)]

    # Iterate over every cell in the grid
    for r in range(rows):
        for c in range(cols):
            live_neighbors = 0
            
            # Check all 8 adjacent neighbors
            for dr in (-1, 0, 1):
                for dc in (-1, 0, 1):
                    # Skip the cell itself
                    if dr == 0 and dc == 0:
                        continue
                    
                    nr, nc = r + dr, c + dc
                    
                    # Ensure the neighbor is within grid boundaries
                    if 0 <= nr < rows and 0 <= nc < cols:
                        live_neighbors += matrix[nr][nc]

            # Apply Conway's rules
            if matrix[r][c] == 1 and live_neighbors in (2, 3):
                next_gen[r][c] = 1
            elif matrix[r][c] == 0 and live_neighbors == 3:
                next_gen[r][c] = 1

    return next_gen
