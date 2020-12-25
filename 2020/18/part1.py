operators = {
    '+': lambda x, y: x + y,
    '*': lambda x, y: x * y
}


def calculate(acc, operator, expr):
    while expr:
        token = expr.pop()
        if token.isdigit():
            acc = operators[operator](acc, int(token))
        elif token in operators.keys():
            operator = token
        elif token == ')':
            return acc
        elif token == '(':
            subresult = calculate(0, '+', expr)
            acc = operators[operator](acc, subresult)
    return acc


print(sum([calculate(0, '+', [c for c in reversed(line.strip()) if c != ' '])
           for line in open('input.txt')]))
