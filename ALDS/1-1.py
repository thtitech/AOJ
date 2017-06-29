import sys

def insert_sort(array):
    for i in range(0, len(array)):
        v = array[i]
        j = i - 1
        while (j >= 0) and (array[j] > v):
            array[j + 1] = array[j]
            j -= 1
        array[j + 1] = v
        print print_list(array)
    return array

def print_list(array):
    s = ""
    for n in array:
        s += str(n) + " "
    s = s.strip()
    return s
    
if __name__ == "__main__":
    array_num = int(sys.stdin.readline().strip())
    array = map(lambda x: int(x), list(sys.stdin.readline().strip().split(" ")))
    array = insert_sort(array)
