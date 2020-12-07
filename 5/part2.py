max_id = 0
seats = []
for line in open('input.txt'):
    line = line.strip()
    row, column = 0, 0
    for c in line[:7]:
        row = (row << 1) + (1 if c == 'B' else 0)
    for c in line[7:]:
        column = (column << 1) + (1 if c == 'R' else 0)

    id = row * 8 + column
    seats.append(id)
    max_id = max(max_id, id)

seats.sort()
for i in range(len(seats)-1):
    if seats[i] != seats[i+1]-1:
        print('missing seat:', seats[i]+1)
