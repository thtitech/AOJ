import sys

def get_left(i):
    return 2 * i + 1

def get_right(i):
    return 2 * i + 2

def get_parent(i):
    return int((i - 1) / 2)

def make_heap_tree(array, i, item_num):
    left = get_left(i)
    right = get_right(i)
    largest = i
    if (left < item_num) and (array[left] > array[largest]):
        largest = left
    if (right < item_num) and (array[right] > array[largest]):
        largest = right
    if largest != i:
        tmp = array[i]
        array[i] = array[largest]
        array[largest] = tmp
        make_heap_tree(array, largest, item_num)

def main():
    size = int(sys.stdin.readline().strip())
    array = map(lambda x: int(x), sys.stdin.readline().strip().split(" "))
    for i in reversed(range(0, get_parent(size) + 1)):
        make_heap_tree(array, i, size)
    print " " + " ".join(map(lambda x: str(x), array))

if __name__ == "__main__":
    main()
