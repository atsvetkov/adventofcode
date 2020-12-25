def parse_data(lines):
    ranges = {}
    my_ticket = []
    nearby_tickets = []
    rules, my, nearby = True, False, False

    for line in lines:
        if line.startswith('your ticket'):
            rules, my, nearby = False, True, False
            continue
        elif line.startswith('nearby tickets'):
            rules, my, nearby = False, False, True
            continue
        if rules:
            parts = line.strip().split(':')
            field = parts[0].strip()
            range_strings = parts[1].strip().split('or')
            valid_values_lists = [list(
                range(int(rs.split('-')[0]), int(rs.split('-')[1])+1)) for rs in range_strings]
            ranges[field] = set([e for l in valid_values_lists for e in l])
        elif my:
            my_ticket = [int(number.strip()) for number in line.split(',')]
        elif nearby:
            nearby_tickets.append([int(number.strip())
                                   for number in line.split(',')])

    return ranges, my_ticket, nearby_tickets


# parse the input
lines = [line.strip('\n') for line in open('input.txt') if line != '\n']
ranges, _, nearby_tickets = parse_data(lines)

# validate tickets
error_rate = 0
for ticket in nearby_tickets:
    for value in ticket:
        valid = False
        for r in ranges.values():
            if valid:
                break
            if value in r:
                valid = True
        if not valid:
            error_rate += value

print(error_rate)
