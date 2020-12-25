def next_departure(bus, earliest_time):
    time = (earliest_time // bus) * bus

    return time if time == earliest_time else time+bus


line1, line2 = [line for line in open('input.txt')]
timestamp = int(line1)
buses = [int(bus.strip()) for bus in line2.split(',') if bus != 'x']

earliest_bus = min([(bus, next_departure(bus, timestamp))
                    for bus in buses], key=lambda x: x[1])

print(earliest_bus[0]*(earliest_bus[1]-timestamp))
