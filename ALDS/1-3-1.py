import sys
import math

if __name__ == "__main__":
    num = int(sys.stdin.readline().strip())
    ans = 0
    for i in range(0, num):
        n = int(sys.stdin.readline().strip())
        flag = False
        for j in range(2, int(math.sqrt(n)) + 1):
            if n % j == 0:
                flag = True
                break
        if not flag:
            ans += 1
    print ans
