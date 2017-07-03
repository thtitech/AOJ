import sys

stack = []

array = sys.stdin.readline().strip().split(" ")

for op in array:
    if op.isdigit():
        stack.append(int(op))
    else:
        tmp1 = stack.pop()
        tmp2 = stack.pop()
        if op == "+":
            stack.append(tmp1 + tmp2)
        elif op == "-":
            stack.append(tmp2 - tmp1)
        elif op == "*":
            stack.append(tmp1 * tmp2)
        elif op == "/":
            stack.append(float(tmp2) / tmp1)
res = stack.pop()
print str(int(res))
