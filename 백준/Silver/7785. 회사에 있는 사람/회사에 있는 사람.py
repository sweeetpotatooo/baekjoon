import sys
input = sys.stdin.readline
n = int(input())
log = {}
for _ in range(n):
    name, status = input().split()
    if status == "enter":
        log[name] = True
    else:
        log.pop(name, None)
current_employees = sorted(log.keys(), reverse=True)
for employee in current_employees:
    print(employee)
    