def manhattan_distance(x, y):
    return abs(x) + abs(y)


def rotate(vector, degrees, direction):
    if direction == -1:
        degrees = 360-degrees

    steps = degrees//90
    for _ in range(steps):
        vector = (vector[1], -vector[0])

    return vector


def move(x, y, instruction, vector):
    command, value = instruction
    if command == 'F':
        x, y = x+vector[0]*value, y+vector[1]*value
    elif command == 'N':
        vector = (vector[0], vector[1]+value)
    elif command == 'S':
        vector = (vector[0], vector[1]-value)
    elif command == 'E':
        vector = (vector[0]+value, vector[1])
    elif command == 'W':
        vector = (vector[0]-value, vector[1])
    elif command == 'R':
        vector = rotate(vector, value, 1)
    elif command == 'L':
        vector = rotate(vector, value, -1)

    return x, y, vector


# starting position and waypoint
x, y = 0, 0

# vector is now the waypoint
vector = (10, 1)

instructions = [(line[0], int(line[1:])) for line in open('input.txt')]

# simulate ship moves
for instruction in instructions:
    x, y, vector = move(x, y, instruction, vector)

print(x, y)
print('manhattan distance:', manhattan_distance(x, y))
