def manhattan_distance(x, y):
    return abs(x) + abs(y)


def rotate(vector, degrees, direction):
    v = [(1, 0), (0, -1), (-1, 0), (0, 1)]
    index = v.index(vector)
    steps = degrees//90

    return v[(index + steps*direction) % 4]


def move(x, y, instruction, vector):
    command, value = instruction
    if command == 'F':
        x, y = x+vector[0]*value, y+vector[1]*value
    elif command == 'N':
        y += value
    elif command == 'S':
        y -= value
    elif command == 'E':
        x += value
    elif command == 'W':
        x -= value
    elif command == 'R':
        vector = rotate(vector, value, 1)
    elif command == 'L':
        vector = rotate(vector, value, -1)

    return x, y, vector


# starting position
x, y = 0, 0

# ship is facing east, i.e. in the direction of increasing X axis
vector = (1, 0)

instructions = [(line[0], int(line[1:])) for line in open('input.txt')]

# simulate ship moves
for instruction in instructions:
    x, y, vector = move(x, y, instruction, vector)

print(x, y)
print('manhattan distance:', manhattan_distance(x, y))
