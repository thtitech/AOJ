import Queue
import sys

class Proc:
    def __init__(self, name, time):
        self.time = time
        self.name = name

def main():
    array = map(lambda x: int(x), sys.stdin.readline().strip().split(" "))
    p_num = array[0]
    q_time = array[1]
    p_queue = Queue.Queue()
    for i in range(0, p_num):
        array = sys.stdin.readline().strip().split(" ")
        p_queue.put(Proc(array[0], int(array[1])))
    t = 0
    while not p_queue.empty():
        p = p_queue.get()
        if p.time > q_time:
            p.time = p.time - q_time
            p_queue.put(p)
            t += q_time
        else:
            t += p.time
            print p.name + " " + str(t)
    
if __name__ == "__main__":
    main()
