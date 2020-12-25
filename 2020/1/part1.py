TARGET = 2020
h = set()

# two-sum algorithm
for line in open('input.txt'):
    num = int(line)
    if TARGET-num in h:
        print(num*(TARGET-num))
        break
    else:
        h.add(num)
