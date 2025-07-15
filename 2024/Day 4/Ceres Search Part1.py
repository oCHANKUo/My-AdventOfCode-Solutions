def count_xmas(grid):
    word = "XMAS"
    rows = len(grid)
    cols = len(grid[0])
    count = 0

    directions = [
        (0, 1),   # right
        (1, 0),   # down
        (0, -1),  # left
        (-1, 0),  # up
        (1, 1),   # down-right
        (1, -1),  # down-left
        (-1, 1),  # up-right
        (-1, -1)  # up-left
    ]

    for i in range(rows):
        for j in range(cols):
            for dx, dy in directions:
                letters = []
                for k in range(4):
                    ni = i + k * dx
                    nj = j + k * dy
                    if 0 <= ni < rows and 0 <= nj < cols:
                        letters.append(grid[ni][nj])
                    else:
                        break
                if "".join(letters) == word:
                    count += 1
    return count

with open(r"C:\Users\chanu\GitHub Projects\My-AdventOfCode-Solutions\2024\Day 4\input.txt") as f:
    lines = [line.strip() for line in f if line.strip()]

grid = [list(line) for line in lines]
print(count_xmas(grid))
