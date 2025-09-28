from collections import deque
import sys
input = sys.stdin.readline
d = deque()
n = int(input())
for _ in range(n):
    cmd = input().strip().split()
    if cmd[0] == "push_front":
        d.appendleft(int(cmd[1]))
    elif cmd[0] == "push_back":
        d.append(int(cmd[1]))
    elif cmd[0] == "pop_front":
        print(d.popleft() if d else -1)
    elif cmd[0] == "pop_back":
        print(d.pop() if d else -1)
    elif cmd[0] == "size":
        print(len(d))
    elif cmd[0] == "empty":
        print(0 if d else 1)
    elif cmd[0] == "front":
        print(d[0] if d else -1)
    elif cmd[0] == "back":
        print(d[-1] if d else -1)
        