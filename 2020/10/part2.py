numbers = sorted([int(line) for line in open('input.txt')])
numbers = [0] + numbers + [numbers[-1]+3]

count = 1
diffs = [numbers[i+1]-numbers[i] for i in range(len(numbers)-1)]

# count ones between threes; since input only contains 1 and 3, there is a finite number of patterns, each contributing a specific number of possible paths until they converge back again
# (an alternative could be a recursive solution with memoization)
ones = 0
for d in diffs:
    if d == 1:
        ones += 1
    if d == 3:
        if ones == 2:
            count *= 2
        elif ones == 3:
            count *= 4
        elif ones == 4:
            count *= 7
        ones = 0

print(count)
