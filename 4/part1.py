fields_mask = {
    'cid': 1 << 0,
    'iyr': 1 << 1,
    'eyr': 1 << 2,
    'hgt': 1 << 3,
    'hcl': 1 << 4,
    'ecl': 1 << 5,
    'pid': 1 << 6,
    'byr': 1 << 7
}

valid_count = 0
total = 0
fields = 0
for line in open('input.txt'):
    if line == '\n':
        if fields >= 254:
            valid_count += 1
        fields = 0
        total += 1
    else:
        pairs = line.split(' ')
        for pair in pairs:
            key = pair.split(':')[0]
            fields |= fields_mask[key]

print(valid_count, 'valid out of', total)
