a= int(input().strip())
b= int(input().strip())

one = b % 10
ten = (b//10) % 10
hundred = b // 100


print(one * a)
print(ten * a)
print(hundred * a)
print(a * b)
