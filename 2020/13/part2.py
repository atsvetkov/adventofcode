import math

_, line2 = [line for line in open('input.txt')]
buses = line2.split(',')
shifts = {}
for index, bus in enumerate(buses):
    if bus == 'x':
        continue

    bus_number = int(bus)
    shifts[bus_number] = index

print(shifts)

num_rem = [(bus, (bus-shift) % bus) for bus, shift in shifts.items()]
num_product = math.prod([nr[0] for nr in num_rem])

print(num_rem)
