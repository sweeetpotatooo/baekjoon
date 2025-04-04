H, R = map(int, input().split())
if R >= 45:
    print(H, R - 45)
else:
    if H == 0:
        print(23, R + 15)
    else:
        print(H - 1, R + 15)

