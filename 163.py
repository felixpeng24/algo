"""
The expression is given as a list of numbers and operands. For example: [5, 3, '+'] should return 5 + 3 = 8.

For example, [15, 7, 1, 1, '+', '-', '/', 3, '*', 2, 1, 1, '+', '+', '-'] should return 5, since it is equivalent to ((15 / (7 - (1 + 1))) * 3) - (2 + (1 + 1)) = 5.

You can assume the given expression is always valid.
"""

def evaluate_rpn(expression):
    stack = []
    
    for token in expression:
        if isinstance(token, int):  # If it's a number, push to stack
            stack.append(token)
        else:  # It's an operator, pop two numbers and apply the operation
            b = stack.pop()
            a = stack.pop()
            if token == '+':
                stack.append(a + b)
            elif token == '-':
                stack.append(a - b)
            elif token == '*':
                stack.append(a * b)
            elif token == '/':  
                stack.append(int(a / b))  # Integer division like in Python 3
        
    return stack[0]  # The final result will be the last remaining element

# Example cases
print(evaluate_rpn([5, 3, '+']))  # Output: 8
print(evaluate_rpn([15, 7, 1, 1, '+', '-', '/', 3, '*', 2, 1, 1, '+', '+', '-']))  # Output: 5
