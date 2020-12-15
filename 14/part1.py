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


mem = {}
for line in open('input.txt'):
    if line.startswith('mask'):
        zero_mask, one_mask = all_ones(36), 0
        mask_string = line.split('=')[1].strip()
        for i, c in enumerate(mask_string):
            if c == '1':
                one_mask = set_bit(one_mask, 35-i)
            elif c == '0':
                zero_mask = clear_bit(zero_mask, 35-i)
    else:
        address_string, value_string = line.split('=')
        address, value = int(address_string.strip().replace(
            'mem[', '').replace(']', '')), int(value_string.strip())
        mem[address] = (value | one_mask) & zero_mask

print(sum(mem.values()))
