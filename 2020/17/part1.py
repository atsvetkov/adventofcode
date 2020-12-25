import collections

def parse_data():
    active_cubes = collections.defaultdict(int)
    x, y, z = 0, 0, 0
    for line in open('input.txt'):
        x = 0
        for c in line:
            state = 1 if c == '#' else 0
            if state == 1:
                active_cubes[(x, y, z)] = 1
            x += 1
        y += 1
    return active_cubes

def get_neighbours(point):
    x, y, z = point
    directions = [
            # along axes
            (1,0,0), (-1,0,0), (0,1,0), (0,-1,0), (0,0,1), (0,0,-1),
            # along diagonals in Z plane
            (1,1,0), (1,-1,0), (-1,1,0), (-1,-1,0),
            # along diagonals in Y plane
            (1,0,1), (1,0,-1), (-1,0,1), (-1,0,-1),
            # along diagonals in X plane
            (0,1,1), (0,1,-1), (0,-1,1), (0,-1,-1),
            # along 3D diagonals
            (1,1,1), (1,1,-1), (1,-1,1), (1,-1,-1),
            (-1,1,1), (-1,1,-1), (-1,-1,1), (-1,-1,-1)]
    
    return [(x+dx,y+dy,z+dz) for dx,dy,dz in directions]

def active_neighbours_count(point, cubes):
    return sum([cubes[neighbour] for neighbour in get_neighbours(point)])

def get_relevant_cubes(cubes):
    result = set()
    for cube in cubes:
        for n in get_neighbours(cube):
            result.add(n)
    return result

def next_state(cubes):
    relevant_cubes = get_relevant_cubes(cubes)
    new_cubes = collections.defaultdict(int)
    for cube in relevant_cubes:
        count = active_neighbours_count(cube, cubes)
        if cubes[cube] == 1:
            new_cubes[cube] = 1 if (count == 2 or count == 3) else 0
        elif cubes[cube] == 0 and count == 3:
            new_cubes[cube] = 1

    return new_cubes 

def count_active(cubes):
    return len([1 for k, v in cubes.items() if v == 1])

cubes = parse_data()
i, cycles = 1, 6
while i <= cycles:
    count_before = count_active(cubes)
    cubes = next_state(cubes)
    count_after = count_active(cubes)
    print(i, ':', count_before, '->', count_after)
    i += 1
