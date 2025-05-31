# Furiosa AI에서는 AI 연산에 최적화된 반도체인 WARBOY란 이름의 NPU(Neural Processing Unit)를 만들고 있다. 
# NPU는 인공지능 모델의 학습 및 추론을 기존의 처리 유닛보다 훨씬 빠르게 할 수 있다.

# WARBOY는 글로벌 AI 반도체 벤치마크 대회의 이미지 분류, 객체 검출 처리 속도 면에서 가장 좋은 성적을 받았다. 
# 특히, WARBOY는 가격 대비 성능이 경쟁사 제품의 3배나 되어 많은 관심을 끌었다.

# 가격 대비 성능은 아래와 같은 수식으로 계산된다.

# 출력
# 첫째 줄에 WARBOY의 성능을 출력한다.

import sys
input = sys.stdin.readline

a,b,c = map(int,input().split())
print(b//a*3*c)