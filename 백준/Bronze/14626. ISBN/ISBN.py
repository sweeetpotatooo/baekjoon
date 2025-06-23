ISBN = input()

check_sign = int(ISBN[-1])

temp_sum = 0
unknown_number_weight = 0

for number, weight in zip(ISBN[:-1], [1, 3] * 6):
    if number == '*':
        unknown_number_weight = weight
        continue

    temp_sum += int(number) * weight

for unknown_number in range(10):
    rest = (temp_sum + (unknown_number * unknown_number_weight) + check_sign) % 10
    
    if rest == 0:
        print(unknown_number)
        break