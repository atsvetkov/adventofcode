valid_count = 0
for line in open('input.txt'):
    space_index = line.index(' ')
    limits = [int(limit) for limit in line[:space_index].split('-')]
    first, second = limits[0]-1, limits[1]-1
    colon_index = line.index(':')
    letter = line[space_index+1:colon_index]
    word = line[colon_index+2:]
    if (word[first] == letter and word[second] != letter) or (word[first] != letter and word[second] == letter):
        valid_count += 1

print("number of valid passwords:", valid_count)
