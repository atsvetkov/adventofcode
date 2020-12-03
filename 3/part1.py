RIGHT, DOWN = 3, 1

rows = [[1 if c == '#' else 0 for c in line[:-1]]
        for line in open('input.txt')]

height, width, trees, row, col = len(rows), len(rows[0]), 0, 0, 0
for row in range(0, height, DOWN):
    trees += rows[row][col]
    col = (col+RIGHT) % width

print(trees)
