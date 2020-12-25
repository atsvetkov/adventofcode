max_id = 0
for line in open('input.txt'):
    line = line.strip()
    row, column = 0, 0
    for c in line[:7]:
        row = (row << 1) + (1 if c == 'B' else 0)
    for c in line[7:]:
        column = (column << 1) + (1 if c == 'R' else 0)

    id = row * 8 + column
    max_id = max(max_id, id)

print(max_id)
