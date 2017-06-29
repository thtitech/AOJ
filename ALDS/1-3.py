import sys

def get_prime_list(max_num):
    res = range(2, max_num + 1)
    for i in range(2, max_num/2 + 1):
        res = filter(lambda x: not ((x % i == 0) and (x != i)), res)        
    return res

if __name__ == "__main__":
    num = int(sys.stdin.readline().strip())
    num_list = [int(sys.stdin.readline().strip()) for i in range(0, num)]
    prime_list = get_prime_list(max(num_list))
    print len(filter(lambda x: x in prime_list, num_list))
    '''
    num_list = [2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17]
    prime_list = get_prime_list(max(num_list))
    print prime_list
    print len(filter(lambda x: x in prime_list, num_list))
    '''
