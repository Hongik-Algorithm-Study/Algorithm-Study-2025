from itertools import permutations

def solution(expression):
    operators = ['+', '-', '*']
    op_orders = permutations(operators, 3)

    def calc(op, a, b):
        if op == '+':
            return str(int(a) + int(b))
        elif op == '-':
            return str(int(a) - int(b))
        else:
            return str(int(a) * int(b))

    max_value = 0

    for order in op_orders:
        temp = []
        num = ''
        for ch in expression:
            if ch in operators:
                temp.append(num)
                temp.append(ch)
                num = ''
            else:
                num += ch
        temp.append(num)

        for op in order:
            stack = []
            i = 0
            while i < len(temp):
                if temp[i] == op:
                    prev = stack.pop()
                    next_num = temp[i + 1]
                    stack.append(calc(op, prev, next_num))
                    i += 2
                else:
                    stack.append(temp[i])
                    i += 1
            temp = stack

        max_value = max(max_value, abs(int(temp[0])))

    return max_value