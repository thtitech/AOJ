import sys

def main():
    linked_list = []
    c_num = int(sys.stdin.readline().strip())
    for i in range(0, c_num):
        line = sys.stdin.readline().strip().split(" ")
        op = line[0]
        if op == "insert":
            linked_list.insert(0, int(line[1]))
        if op == "delete":
            for (i, num) in enumerate(linked_list):
                if int(line[1]) == num:
                    linked_list.pop(i)
                    break
        if op == "deleteFirst":
            linked_list.pop(0)
        if op == "deleteLast":
            linked_list.pop()
    s = ""
    for i in linked_list:
        s += str(i) + " "
    print s.strip()
    
if __name__ == "__main__":
    main()
