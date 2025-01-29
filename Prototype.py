
"""
This is the python prototype of the calculator. It is a simple calculator that can evaluate arithmetic expressions with 
the following operators: +, -, *, /, ^. It uses the Shunting Yard algorithm to convert infix expressions to postfix notation 
and then evaluates the postfix expression using a stack. I will convert this code to C++ and add a GUI to it (later if I have time).
""" 
precedence = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}
associativity = {'+': 'L', '-': 'L', '*': 'L', '/': 'L', '^': 'R'}

def shunting_yard(expression):
    output = []
    stack = []
    for item in expression.split():
        if item.isnumeric():
            output.append(item)
        elif item in precedence:
            while stack and stack[-1] in precedence and (precedence[stack[-1]] > precedence[item] or (precedence[stack[-1]] == precedence[item] and associativity[item] == 'L')):
                output.append(stack.pop())
            stack.append(item)
    while stack:
        output.append(stack.pop())
    return ' '.join(output)

def evaluate(expression):
    stack = []
    for item in expression.split():
        if item.isnumeric():
            stack.append(int(item))
        elif item in precedence:
            b = stack.pop()
            a = stack.pop()
            if item == '+':
                stack.append(a + b)
            elif item == '-':
                stack.append(a - b)
            elif item == '*':
                stack.append(a * b)
            elif item == '/':
                stack.append(a / b)
            elif item == '^':
                stack.append(a ** b)
    return stack.pop()

def main():
    expression = input("Enter an expression: ")
    print("Expression:", expression)
    postfix = shunting_yard(expression)
    print("Postfix:", postfix)
    print("Result:", evaluate(postfix))

main()




