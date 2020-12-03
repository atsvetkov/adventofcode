valid_count = 0
for line in open('input.txt'):
    space_index = line.index(' ')
    limits = [int(limit) for limit in line[:space_index].split('-')]
    lo, hi = limits[0], limits[1]
    colon_index = line.index(':')
    letter = line[space_index+1:colon_index]
    word = line[colon_index+1:]
    letter_count = 0
    for c in word:
        if c == letter:
            letter_count += 1
            if letter_count > hi:
                break
    if lo <= letter_count <= hi:
        valid_count += 1

print("number of valid passwords:", valid_count)
