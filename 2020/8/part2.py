def swap(program, index):
    instruction, value = program[index]
    if instruction == 'jmp':
        program[index] = ('nop', value)
    elif instruction == 'nop':
        program[index] = ('jmp', value)


instruction_set = {
    'nop': lambda index, accumulator, value: (index+1, accumulator),
    'acc': lambda index, accumulator, value: (index+1, accumulator+value),
    'jmp': lambda index, accumulator, value: (index+value, accumulator)
}

program = [(line.split(' ')[0].strip(), int(line.split(' ')[1].strip()
                                            ))
           for line in open('input.txt')]

n = len(program)
index_to_try, last_tried_index = 0, -1
done = False
while index_to_try < n:
    if done:
        break

    swap(program, index_to_try)
    infinite_loop = False
    index, accumulator, executed = 0, 0, set()
    while True:
        if index in executed:
            infinite_loop = True
            break

        if index == n:
            print('corruption fixed. accumulator:', accumulator)
            done = True
            break

        executed.add(index)
        instruction, value = program[index]
        index, accumulator = instruction_set[instruction](
            index, accumulator, value)

    if infinite_loop:
        swap(program, index_to_try)
        index_to_try += 1
