import sys
import math

def get_prime_list(max_num):
    res = list(range(2, max_num + 1))
    for i in range(2, int(math.sqrt(max_num)) + 1):
        res = list(filter(lambda x: not ((x % i == 0) and (x != i)), res))
    return res

def is_include(array, num):
    right = len(array) - 1
    left = 0
    while right >= left:
        index = (right + left) / 2
        if array[index] == num:
            return True
        elif array[index] < num:
            left = index + 1
        elif array[index] > num:
            right = index - 1
    return False

if __name__ == "__main__":
    num = int(sys.stdin.readline().strip())
    num_list = [int(sys.stdin.readline().strip()) for i in range(0, num)]
    prime_list = sorted(get_prime_list(max(num_list)))
    print (len(list(filter(lambda x: x in prime_list, num_list))))
