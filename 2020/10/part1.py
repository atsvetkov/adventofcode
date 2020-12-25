from collections import defaultdict

numbers = sorted([int(line) for line in open('input.txt')])
numbers.append(numbers[-1]+3)
joltage, current, counter = 0, 0, defaultdict(int)
for number in numbers:
    counter[number-current] += 1
    current = number

print(counter[1]*counter[3])
