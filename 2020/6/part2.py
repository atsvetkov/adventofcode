total, qq = 0, []
for line in open('input.txt'):
    if line == '\n':
        total += len(set.intersection(*qq))
        qq = []
    else:
        qq.append(set(line.strip()))

print(total)
