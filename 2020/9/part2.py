def has_two_sum(numbers, target):
    h = set()
    for num in numbers:
        if target-num in h:
            return True
        else:
            h.add(num)

    return False


# find the first wrong number
SIZE = 25
numbers = [int(line) for line in open('input.txt')]
window = numbers[:SIZE]
wrong_number = None
for number in numbers[SIZE:]:
    if not has_two_sum(window, number):
        wrong_number = number
        break
    else:
        window = window[1:] + [number]

print('wrong number:', wrong_number)

# find the contigous subarray with target sum (lazy O(n^2) algorithm)
partial_sum = [0]
for i in range(len(numbers)):
    partial_sum.append(partial_sum[i]+numbers[i])

for i in range(len(numbers)-1):
    for j in range(i+1, len(numbers)):
        if wrong_number == partial_sum[j+1]-partial_sum[i]:
            print(min(numbers[i:j+1])+max(numbers[i:j+1]))
