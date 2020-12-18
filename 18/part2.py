# define operators as (precedence, function) tuples
operators = {
    '+': (1, lambda x, y: x + y),
    '*': (0, lambda x, y: x * y)
}


def to_postfix(expr):
    """Convert expression (with no whitespaces anymore) to postfix ("Reverse Polish") notation"""
    q, ops = [], []
    for token in expr:
        if token.isdigit():
            q.append(token)
        elif token in operators.keys():
            while ops and ops[-1] in operators and operators[ops[-1]][0] > operators[token][0]:
                q.append(ops.pop())
            ops.append(token)
        elif token == '(':
            ops.append(token)
        elif token == ')':
            while ops and ops[-1] != '(':
                q.append(ops.pop())
            if ops and ops[-1] == '(':
                ops.pop()

    while ops:
        q.append(ops.pop())

    return q


def calculate(infix):
    """Calculate the result of an expression in postfix notation"""
    s = []
    for token in infix:
        if token.isdigit():
            s.append(int(token))
        else:
            op1, op2 = s.pop(), s.pop()
            s.append(operators[token][1](op1, op2))

    return s[0]


print(sum([calculate(to_postfix([c for c in line.strip() if c != ' ']))
           for line in open('input.txt')]))
