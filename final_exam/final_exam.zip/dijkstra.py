import re
import stack
import bitree
import typing


def is_num(s):
    """
    Returns True if and only if s can be parsed as an integer
    :param s: the string to test
    :return: True if and only if s can be parsed as an integer
    DO NOT CHANGE THIS CODE!
    """
    try:
        int(s)
        return True
    except ValueError:
        return False


def to_num(s: str):
    """
    If s can be parsed as an integer, return the result of the parse,
    otherwise, return s without conversion
    :param s: the string to try to convert to a number
    :return: if s can be parsed as an integer, return the result of the parse,
             otherwise, return s without conversion
    DO NOT CHANGE THIS CODE!
    """
    try:
        return int(s)
    except ValueError:
        return s


def tokenize(exp: str) -> typing.List:
    tokens = re.findall(r'\d+|\S', exp)
    # Convert numeric tokens to integers
    for i, token in enumerate(tokens):
        if token.isdigit():
            tokens[i] = int(token)
        elif token == '-':
            # Check if the '-' is a unary operator or a subtraction operator
            if i == 0 or tokens[i - 1] in ['(', '+', '-', '*', '/']:
                # Treat '-' as unary negation
                tokens[i] = -1
                tokens.insert(i + 1, '*')  # Insert a multiplication operator
    return tokens

def is_op(s):
    """
    Returns True iff s is an operator
    :param s: the string to test
    :return: True iff s is an operator, and False, otherwise
    DO NOT CHANGE THIS CODE!

    >>> is_op('+')
    True
    >>> is_op('-')
    True
    >>> is_op('*')
    True
    >>> is_op('/')
    True
    >>> import random
    >>> ascii = ord('+')
    >>> while chr(ascii) in '+-*/':
    ...     ascii = random.randint(0, 255)
    >>> is_op(chr(ascii))
    False
    """
    return str(s) in '+-*/'


def precedence(op: str):
    """
    Returns the precedence value of the specified operator
    :param op: the operator
    :return: the precedence value of the specified operator,
             and False, if it is not one of the four
    DO NOT CHANGE THIS CODE!
    """
    precs = {
        '+': 2,
        '-': 2,
        '*': 3,
        '/': 3
    }
    return precs.get(op, False)


def to_rpn(expr: str):
    precedence = {'+': 2, '-': 2, '*': 3, '/': 3}
    output = []
    op_stack = []
    for token in tokenize(expr):
        if isinstance(token, int):
            output.append(str(token))
        elif token == '(':
            op_stack.append(token)
        elif token == ')':
            while op_stack and op_stack[-1] != '(':
                output.append(op_stack.pop())
            op_stack.pop()  # Discard the '('
        else:
            while op_stack and precedence.get(op_stack[-1], 0) >= precedence[token]:
                output.append(op_stack.pop())
            op_stack.append(token)
    while op_stack:
        output.append(op_stack.pop())
    return ' '.join(output)

def to_ast(expr: str):
    def add_node(stack, op):
        right = stack.pop()
        if op == '-':
            # Unary negation, create a NegateNode
            stack.push(bitree.NegateNode(right))
        else:
            left = stack.pop()
            stack.push(bitree.DataNode(op, left, right))

    operator_stack = stack.LRStack()
    operand_stack = stack.LRStack()
    toks = [to_num(t) for t in tokenize(expr)]
    for tok in toks:
        if is_num(tok):
            operand_stack.push(bitree.DataNode(tok))
        elif is_op(tok):
            while (not operator_stack.is_empty()) and precedence(operator_stack.top()) >= precedence(tok):
                add_node(operand_stack, operator_stack.pop())
            operator_stack.push(tok)
        elif tok == '(':
            operator_stack.push(tok)
        elif tok == ')':
            while (not operator_stack.is_empty()) and operator_stack.top() != '(':
                add_node(operand_stack, operator_stack.pop())
            if operator_stack.is_empty():
                print('Unbalanced parentheses')
                return None
            operator_stack.pop()  # Discard '('
    while not operator_stack.is_empty():
        add_node(operand_stack, operator_stack.pop())
    return operand_stack.pop()

def eval_rpn(expr: str):
    stack = []
    for token in expr.split():
        if token.isdigit():
            stack.append(int(token))
        else:
            num2 = stack.pop()
            num1 = stack.pop()
            if token == '+':
                stack.append(num1 + num2)
            elif token == '-':
                stack.append(num1 - num2)
            elif token == '*':
                stack.append(num1 * num2)
            elif token == '/':
                stack.append(num1 // num2)  # Integer division
    return stack.pop()

if __name__ == '__main__':
    # This is here for your own use
    pass
