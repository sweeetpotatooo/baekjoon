import sys
input = sys.stdin.readline

plus, minus = map(int, input().split())


team1 = (plus + minus) // 2
team2 = (plus - minus) // 2

if (team1 < 0 or team2 < 0) or ((plus + minus) % 2 != 0) or ((plus - minus) % 2 != 0):
    print(-1)
else:
    print(team1, team2)
