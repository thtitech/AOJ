import sys

d_num = int(sys.stdin.readline().strip())

graph_list = []

for _ in range(0, d_num):
    array = sys.stdin.readline().strip().split(" ")
    if len(array) <= 2:
        graph_list.append([])
    else:
        graph_list.append([int(array[i]) - 1 for i in range(2, len(array))])

t = 1
result = [[] for _ in range(0, d_num)]
searched_list = []
stack = []

while True:
    if len(stack) == 0:
        ll = filter(lambda x: x not in searched_list, range(0, d_num))
        if len(ll) == 0:
            break
        stack.append(ll[0])
        result[ll[0]].append(t)
        searched_list.append(ll[0])
    else:
        node = stack[-1]
        children = filter(lambda x: x not in searched_list, graph_list[node])
        if len(children) != 0:
            next_node = children[0]
            stack.append(next_node)
            result[next_node].append(t)
            searched_list.append(next_node)
        else:
            stack.pop()
            result[node].append(t)
    t += 1

s = ""

for i in range(0, len(result)):
    print str(i+1) + " " + str(result[i][0]) + " " + str(result[i][1])
    
            
