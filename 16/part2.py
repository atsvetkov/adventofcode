import math


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


def get_valid_tickets(tickets, values):
    for ticket in tickets:
        invalid = False
        for value in ticket:
            if value not in values:
                invalid = True
                break
        if not invalid:
            yield ticket


def is_valid_field_index(field_name, index, tickets, ranges):
    for ticket in tickets:
        value = ticket[index]
        if value not in ranges[field_name]:
            # print('  NO:', value, 'not in', ranges[field_name])
            return False

    return True


def get_sorted_possible_fields(fields, tickets, ranges):
    possible_fields = []
    for i in range(len(fields)):
        possible_fields.append((i, set([field for field in fields if is_valid_field_index(field, i,
                                                                                          list(tickets) + [ticket], ranges)])))
    possible_fields.sort(key=lambda x: len(x[1]))
    return possible_fields


# parse the input
lines = [line.strip('\n') for line in open('input.txt') if line != '\n']
ranges, ticket, nearby_tickets = parse_data(lines)

# eliminate invalid tickets, add my ticket to the remaining valid ones
valid_tickets = list(get_valid_tickets(nearby_tickets, set(
    [r for range in ranges.values() for r in range])))
valid_tickets.append(ticket)
fields = list(ranges.keys())

# test possible fields for every index in the tickets
possible_fields = get_sorted_possible_fields(fields, valid_tickets, ranges)

# start eliminating obvious fields one by one
result, used = {}, set()
for index, fields in possible_fields:
    options = fields-used
    if len(options) == 1:
        field = options.pop()
        used.add(field)
        result[field] = index

print(math.prod([ticket[result[field]]
                 for field in fields if field.startswith('departure')]))
