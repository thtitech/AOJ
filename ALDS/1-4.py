import sys

num = int(sys.stdin.readline().strip())

r0 = int(sys.stdin.readline().strip())
r1 = int(sys.stdin.readline().strip())

max_dis = r1 - r0
min_num = min(r0, r1)

for i in range(0, num-2):
    r = int(sys.stdin.readline().strip())
    max_dis = max(max_dis, r - min_num)
    min_num = min(min_num, r)

print max_dis

