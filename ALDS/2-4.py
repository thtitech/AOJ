import sys

STEP = 2

def insert_sort(array, step, cnt):
    for i in range(step, len(array)):
        v = array[i]
        j = i - step
        while (j >= 0) and (array[j] > v):
            array[j + step] = array[j]
            j = j - step
            cnt += 1
        array[j + step] = v
    return cnt

def shell_sort(array):
    cnt = 0
    v = int(len(array)/STEP)
    step_list = []
    while v > 0:
        step_list.append(v)
        v = int(v/STEP)
    if len(step_list) == 0:
        step_list.append(1)
    for step in step_list:
        cnt = insert_sort(array, step, cnt)
    return (cnt, step_list)

def list_to_string(array):
    s = ""
    for n in array:
        s += str(n) + " "
    return s.strip()

def main():
    num = int(sys.stdin.readline().strip())
    array = [int(sys.stdin.readline().strip()) for i in range(0, num)]
    c = shell_sort(array)
    print str(len(c[1]))
    print list_to_string(c[1])
    print str(c[0])
    for n in array:
        print str(n)

if __name__ == "__main__":
    main()
