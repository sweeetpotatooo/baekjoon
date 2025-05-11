import sys
input = sys.stdin.readline

first = int(input())
second = int(input())
third = int(input())

if (first+ second+ third != 180):
  print("Error") 
elif (first==60 & second== 60 & third ==60):
  print("Equilateral")
elif (first != second & second != third & third != first):
  print("Scalene")
else:
  print("Isosceles")