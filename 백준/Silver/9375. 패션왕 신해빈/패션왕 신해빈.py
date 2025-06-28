import sys
from collections import defaultdict
input = sys.stdin.readline
def count_outfits(test_cases):
    results = []
    for _ in range(test_cases):
        n = int(input())
        if n == 0:
            results.append(0)
            continue
        
        clothes = defaultdict(int)
        for _ in range(n):
            _, kind = input().split()
            clothes[kind] += 1
        
        # 각 종류의 의상 수 + 1 (안 입는 경우 포함)
        outfit_count = 1
        for count in clothes.values():
            outfit_count *= (count + 1)
        
        # 알몸인 경우를 제외
        results.append(outfit_count - 1)
    
    return results
if __name__ == "__main__":
    test_cases = int(input())
    results = count_outfits(test_cases)
    for result in results:
        print(result)