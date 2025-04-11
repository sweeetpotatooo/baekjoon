import sys
input = sys.stdin.readline

grade = {
    'A+': 4.5,
    'A0': 4.0,
    'B+': 3.5,
    'B0': 3.0,
    'C+': 2.5,
    'C0': 2.0,
    'D+': 1.5,
    'D0': 1.0,
    'F': 0.0
}

total_score = 0.0
total_credit = 0.0

for _ in range(20):
    name, credit_str, grade_str = input().split()
    credit = float(credit_str)
    if grade_str == 'P':
        continue
    total_score += credit * grade[grade_str]
    total_credit += credit

if total_credit == 0:
    print(0.0)
else:
    print("{:.6f}".format(total_score / total_credit))
