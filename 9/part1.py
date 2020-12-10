def has_two_sum(numbers, target):
    h = set()
    for num in numbers:
        if target-num in h:
            return True
        else:
            h.add(num)

    return False


SIZE = 25
numbers = [int(line) for line in open('input.txt')]
window = numbers[:SIZE]
for number in numbers[SIZE:]:
    if not has_two_sum(window, number):
        print('wrong number', number)
        break
    else:
        window = window[1:] + [number]
