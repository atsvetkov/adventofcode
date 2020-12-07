TARGET = 2020

numbers = [int(line) for line in open('input.txt')]
numbers.sort()

for i in range(len(numbers)-2):
    num = numbers[i]
    if num >= TARGET:
        break

    subtarget = TARGET-num
    left, right = i+1, len(numbers)-1
    while left < right:
        s = numbers[left] + numbers[right]
        if s == subtarget:
            print(num*numbers[left]*numbers[right])
            break
        elif s < subtarget:
            left += 1
        else:
            right -= 1
