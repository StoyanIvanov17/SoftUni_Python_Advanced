
def is_balanced(parentheses):
    stack = []
    for char in parentheses:
        if char == '(' or char == '{' or char == '[':
            stack.append(char)
        elif len(stack) <= 0:
            return 'NO'
        elif char == ')' and stack.pop() != '(':
            return 'NO'
        elif char == ']' and stack.pop() != '[':
            return 'NO'
        elif char == '}' and stack.pop() != '{':
            return 'NO'

    if len(stack) == 0:
        return 'YES'
    return 'NO'


parentheses = input()
print(is_balanced(parentheses))