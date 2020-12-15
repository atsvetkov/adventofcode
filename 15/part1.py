numbers = [int(c) for c in [line for line in open('input.txt')]
           [0].strip().split(',')]

when = {number: (i+1) for i, number in enumerate(numbers)}
recent_number, age = numbers[-1], 0
turn = len(numbers)+1
while turn <= 2020:
    recent_number, age,  = age, turn-when[age] if age in when else 0
    when[recent_number] = turn
    turn += 1

print(recent_number)
