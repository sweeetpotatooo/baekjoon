nums = list(map(int, input().split()))
if nums == list(range(1, 9)):
    print("ascending")
elif nums == list(range(8, 0, -1)):
    print("descending")
else:
    print("mixed")