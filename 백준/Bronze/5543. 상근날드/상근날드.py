import sys
input = sys.stdin.readline

sangduk = int(input())
jungduk = int(input())
haduk   = int(input())

coke = int(input())
cider = int(input())
setmenu = [sangduk+coke, jungduk+coke, haduk+coke, sangduk +cider, jungduk + cider ,haduk +cider]

print(min(setmenu)-50)