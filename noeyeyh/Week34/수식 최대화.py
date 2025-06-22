import re
from itertools import permutations

def calc(op, a, b):
    a, b = int(a), int(b)
    if op == '+':
        return str(a + b)
    elif op == '-':
        return str(a - b)
    elif op == '*':
        return str(a * b)

def solution(expression):
    # 1. 숫자와 연산자들을 각각 나누어 리스트로 만든 것
    elements = re.findall(r'\d+|[+\-*]', expression)

    # 2. 수식에 실제 포함된 연산자만 추출
    ops = set(filter(lambda x: x in "+-*", elements))

    # 3. 연산자 우선순위 조합 생성
    priority_orders = permutations(ops)

    max_result = 0

    # 4. 모든 우선순위 조합 시도
    for order in priority_orders:
        exp = elements[:]

        for op in order:
            stack = []
            while exp:
                element = exp.pop(0)
                if element == op:
                    prev = stack.pop()
                    next_element = exp.pop(0)
                    result = calc(op, prev, next_element)
                    stack.append(result)
                else:
                    stack.append(element)
            exp = stack 

        max_result = max(max_result, abs(int(exp[0])))  # 절댓값 비교

    return max_result
