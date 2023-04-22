def solveExpression(expression):
    def evalExpression(num1, op, num2):
        # Evaluate the expression based on the operator
        if op == '+':
            return num1 + num2
        elif op == '-':
            return num1 - num2
        elif op == '*':
            return num1 * num2
        else:
            return None

    # Check if '?' is in the expression
    if '?' not in expression:
        left, right = expression.split("=")
        if '+' in left:
            op = '+'
            num1, num2 = left.split('+')
        elif '-' in left:
            op = '-'
            num1, num2 = left.split('-')
        elif '*' in left:
            op = '*'
            num1, num2 = left.split('*')
        return int(right) if evalExpression(int(num1), op, int(num2)) == int(right) else -1

    # Split the expression into two parts: left side, right side
    left, right = expression.split("=")

    # Split the left side by the operator to get the two numbers
    if '+' in left:
        op = '+'
        num1, num2 = left.split('+')
    elif '-' in left:
        op = '-'
        num1, num2 = left.split('-')
    elif '*' in left:
        op = '*'
        num1, num2 = left.split('*')

    # Replace the unknown digits with 0-9 and keep track of the original position of the unknown digit
    for i in range(10):
        temp_num1 = num1.replace('?', str(i)) if '?' in num1 else num1
        temp_num2 = num2.replace('?', str(i)) if '?' in num2 else num2
        temp_right = right.replace('?', str(i)) if '?' in right else right

        if evalExpression(int(temp_num1), op, int(temp_num2)) == int(temp_right):
            return i
    return -1


# Unit tests
print(solveExpression("1+2=3"))  # Output: 3
print(solveExpression("1+2=?"))  # Output: 3
print(solveExpression("?+2=3"))  # Output: 1
print(solveExpression("1+?=3"))  # Output: 2
print(solveExpression("1-2=?"))  # Output: -1








