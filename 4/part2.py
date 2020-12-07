import re

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

colors = set(['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'])
is_valid = {
    'byr': lambda x: 1920 <= int(x) <= 2002,
    'iyr': lambda x: 2010 <= int(x) <= 2020,
    'eyr': lambda x: 2020 <= int(x) <= 2030,
    'hgt': lambda x: (x[-2:] == 'cm' and (150 <= int(x[:-2]) <= 193)) or (x[-2:] == 'in' and (59 <= int(x[:-2]) <= 76)),
    'hcl': lambda x: x[0] == '#' and re.match(r'[a-f0-9]{6}', x[1:]),
    'ecl': lambda x: x in colors,
    'pid': lambda x: re.match(r'[0-9]{9}', x),
    'cid': lambda _: True
}

valid_count = 0
fields = 0
all_valid = True
valid_fields = 0
pairs = []
for line in open('input.txt'):
    if line == '\n':
        for key, val in pairs:
            fields |= fields_mask[key]

        if fields >= 254:
            for key, val in pairs:
                value_is_valid = is_valid[key](val)
                all_valid = all_valid and value_is_valid

            if fields >= 254 and all_valid:
                valid_count += 1

        fields = 0
        all_valid = True
        valid_fields = 0
        pairs = []
    else:
        local_pairs = [(kv.split(':')[0].strip(), kv.split(':')
                        [1].strip()) for kv in line.split(' ')]
        pairs += local_pairs

print(valid_count)
