room_number = input().strip()
count = [0] * 10 
for digit in room_number:
    num = int(digit)
    if num == 6 or num == 9:
        count[6] += 1
    else:
        count[num] += 1
count[6] = (count[6] + 1) // 2
print(max(count))