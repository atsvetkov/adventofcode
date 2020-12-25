instruction_set = {
    'nop': lambda index, accumulator, value: (index+1, accumulator),
    'acc': lambda index, accumulator, value: (index+1, accumulator+value),
    'jmp': lambda index, accumulator, value: (index+value, accumulator)
}

program = [(line.split(' ')[0].strip(), int(line.split(' ')[1].strip()
                                            ))
           for line in open('input.txt')]

index, accumulator, executed = 0, 0, set()
while index not in executed:
    executed.add(index)
    instruction, value = program[index]
    index, accumulator = instruction_set[instruction](
        index, accumulator, value)

print(accumulator)
