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

flag = True
swap_num = 0

while flag:
    flag = False
    for i in reversed(range(1, len(array))):
        if array[i] < array[i - 1]:
            swap(array, i, i-1)
            flag = True
            swap_num += 1
            
print list_to_string(array)
print str(swap_num)
