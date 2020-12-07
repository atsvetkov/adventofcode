total, q = 0, set()
for line in open('input.txt'):
    if line == '\n':
        total += len(q)
        q = set()
    else:
        for c in line.strip():
            q.add(c)

print(total)
