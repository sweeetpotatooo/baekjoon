s = input().strip()
count = 0
prev_char = ' '

for char in s:
    if char != ' ' and prev_char == ' ':
        count += 1
    prev_char = char

print(count)
