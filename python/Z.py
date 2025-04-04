N, r, c = map(int, input().split())
count = 0

while N != 0:
    N -= 1
    cell = 2**N


    # 1사분면
    if r < cell and c < cell:
        count += cell*cell*0  

    # 2사분면
    elif r < cell and c >= cell:
        count += cell*cell*1
        c -= (cell)

    # 3사분면
    elif r >= cell and c < cell:
        count += cell*cell*2
        r -= (cell)

    # 4사분면
    else:
        count += cell*cell*3
        r -= (cell)
        c -= (cell)
print(count)