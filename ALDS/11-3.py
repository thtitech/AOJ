import sys
import Queue

d_num = int(sys.stdin.readline().strip())

graph_list = []

for _ in range(0, d_num):
    array = sys.stdin.readline().strip().split(" ")
    if len(array) <= 2:
        graph_list.append([])
    else:
        graph_list.append([int(array[i]) - 1 for i in range(2, len(array))])

result = [0 for _ in range(0, d_num)]
searched_list = []
queue = Queue.Queue()

queue.put((0, 0))
searched_list.append(0)
while not queue.empty():
    data = queue.get()
    node = data[0]
    d = data[1]
    children = filter(lambda x: x not in searched_list, graph_list[node])
    for c in children:
        queue.put((c, d + 1))
        searched_list.append(c)
        result[c] = d + 1

for i in range(0, len(result)):
    if (i != 0) and (result[i] == 0):
        print str(i + 1) + " " + str(-1)
    else:
        print str(i + 1) + " " + str(result[i])
            
