def all_ones(bit_count):
    number = 1
    while bit_count > 0:
        number = (number << 1) + 1
        bit_count -= 1

    return number


def set_bit(number, offset):
    mask = 1 << offset
    return number | mask


def clear_bit(number, offset):
    mask = ~(1 << offset)
    return number & mask


def get_floating_addresses(address, bits):
    addresses = []

    def rec(address, index):
        if index == len(bits):
            addresses.append(address)
        else:
            rec(clear_bit(address, bits[index]), index+1)
            rec(set_bit(address, bits[index]), index+1)

    rec(address, 0)

    return addresses


def parse_mask(mask):
    one_mask, bits = 0, []
    for i, c in enumerate(mask):
        if c == '1':
            one_mask = set_bit(one_mask, 35-i)
        elif c == 'X':
            bits.append(35-i)

    return one_mask, bits


mem = {}
for line in open('input.txt'):
    if line.startswith('mask'):
        mask_string = line.split('=')[1].strip()
        one_mask, bits = parse_mask(mask_string)
    else:
        address_string, value_string = line.split('=')
        address, value = int(address_string.strip().replace(
            'mem[', '').replace(']', '')), int(value_string.strip())
        address = address | one_mask
        for a in get_floating_addresses(address, bits):
            mem[a] = value

print(sum(mem.values()))
