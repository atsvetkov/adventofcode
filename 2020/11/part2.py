def get_seat_code(c):
    if c == 'L':
        return 0
    elif c == '.':
        return None
    elif c == '#':
        return 1


def visible_sum(seats, r, c):
    directions = [(1, 0), (0, 1), (-1, 0), (0, -1),
                  (1, -1), (-1, 1), (1, 1), (-1, -1)]
    visible_sum = 0
    for d in directions:
        row, col = r, c
        while True:
            row, col = row + d[0], col + d[1]
            if row < 0 or row >= len(seats) or col < 0 or col >= len(seats[0]):
                break

            if seats[row][col] is None:
                continue
            else:
                visible_sum += seats[row][col]
                break

    return visible_sum


def simulate(seats):
    changes = []
    for r in range(len(seats)):
        for c in range(len(seats[0])):
            seat = seats[r][c]
            if seat is None:
                continue
            vis_sum = visible_sum(seats, r, c)
            if seat == 0 and vis_sum == 0:
                changes.append((r, c, 1))
            elif seat == 1 and vis_sum >= 5:
                changes.append((r, c, 0))

    return changes


def apply_changes(seats, changes):
    for row, col, value in changes:
        seats[row][col] = value


seats = []
for line in open('input.txt'):
    seats.append([get_seat_code(c) for c in line.strip()])

while True:
    changes = simulate(seats)
    if len(changes) == 0:
        print('no seat changes!')
        break

    print(len(changes), 'seat changes')
    apply_changes(seats, changes)

occupied_seats_count = sum(
    [sum([1 if c == 1 else 0 for c in row]) for row in seats])
print(occupied_seats_count, 'occupied seats')
