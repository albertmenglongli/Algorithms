import re
import math
from collections import deque

s = '((2+sin(0))*(3.0+(4*5.0)))'
s = '((cos(2)+sin(sin(1)))*(3.0+(4*5.0)))'


def cal(*args):
    if len(args) == 1:
        return float(args[0])
    elif len(args) == 3:
        num1, operator, num2 = args
        # print(num1, operator, num2)
        return eval(str(num1) + operator + str(num2))


split_lst = re.split(r'([+|-|*|/|(|)])', s)
split_lst = [s for s in split_lst if s]

for i, e in enumerate(split_lst):
    if e in {'sin', 'cos'}:
        split_lst[i] = e + '('
        split_lst[i + 1] = ''

split_lst = [s for s in split_lst if s]

is_left = lambda x: x in {'(', 'sin(', 'cos('}
is_right = lambda x: x == ')'

operators = {'+', '-', '*', '/', 'sin', 'cos'}

original_q = deque()
original_q.extend(split_lst)

stack = deque()

stack.append(original_q.popleft())

while len(original_q) != 0:
    e = original_q.popleft()
    if not is_right(e):
        stack.append(e)
    else:
        # current we encounter a )
        tmp_holders = deque()

        while not is_left(stack[-1]):
            tmp_holders.appendleft(stack.pop())

        value = cal(*tmp_holders)
        left = stack.pop()
        if left.startswith('('):
            stack.append(value)
        elif left.startswith('sin('):
            stack.append(math.sin(value))
        elif left.startswith('cos('):
            stack.append(math.cos(value))

final_res = stack[0]

print(final_res)
