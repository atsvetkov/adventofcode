operators = {
    '+': (1, lambda x, y: x + y),
    '*': (0, lambda x, y: x * y)
}

def calculate(expr):
    nums, ops = [], []
    for token in expr:
        if token.isdigit():
            nums.append(int(token))
        elif token in operators.keys():
            if 

for line in open('input.txt'):
    result = calculate([c for c in reversed(line.strip()) if c != ' '])
    print(f'{line.strip()} ---> {result}')

print(sum([calculate([c for c in reversed(line.strip()) if c != ' ']) for line in open('input.txt')]))