rows = [[1 if c == '#' else 0 for c in line[:-1]]
        for line in open('input.txt')]

height, width, result = len(rows), len(rows[0]), 1
steps = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
for right, down in steps:
    trees, row, col = 0, 0, 0
    for row in range(0, height, down):
        trees += rows[row][col]
        col = (col+right) % width
    result *= trees

print(result)
