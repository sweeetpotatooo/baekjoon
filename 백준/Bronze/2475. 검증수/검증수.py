n= list(map(int, input().split()))
print(sum(x**2 for x in n)%10)
