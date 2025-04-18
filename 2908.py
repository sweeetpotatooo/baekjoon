num1, num2 = map(int, input().split())
r_num1 = int(str(num1)[::-1])
r_num2 = int(str(num2)[::-1])
print(r_num1 if r_num1 > r_num2 else r_num2)