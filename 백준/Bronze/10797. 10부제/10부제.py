import sys
input = sys.stdin.readline

date_last_digit = int(input().strip())
car_last_digits = list(map(int, input().strip().split()))

violating_cars = 0
for car_last_digit in car_last_digits:
    if car_last_digit == date_last_digit:
        violating_cars += 1

print(violating_cars)