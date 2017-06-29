import sys

def get_gcd(x, y):
    if (x % y == 0) or (y % x == 0):
        return min(x, y)
    return get_gcd((max(x, y) % min(x, y)), min(x, y))

if __name__ == "__main__":
    array = map(lambda x: int(x), sys.stdin.readline().strip().split(" "))
    print get_gcd(array[0], array[1])
    
