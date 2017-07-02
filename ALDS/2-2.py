import sys

def swap(a, i, j):
    tmp = a[j]
    a[j] = a[i]
    a[i] = tmp

def list_to_string(a):
    s = ""
    for n in a:
        s += str(n) + " "
    return s.strip()

num = int(sys.stdin.readline().strip())

array = map(lambda x: int(x), sys.stdin.readline().strip().split(" "))

swap_num = 0

for start_index in range(0, len(array)):
    min_index = start_index
    for index in range(start_index, len(array)):
        if array[min_index] > array[index]:
            min_index = index
    if min_index != start_index:
        swap(array, min_index, start_index)
        swap_num += 1
        

print list_to_string(array)
print str(swap_num)
            


