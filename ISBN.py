# ISBN(International Standard Book Number)은 전 세계 모든 도서에 부여된 고유번호로, 
# 국제 표준 도서번호이다. ISBN에는 국가명, 발행자 등의 정보가 담겨 있으며 13자리의 숫자로 표시된다. 
# 그중 마지막 숫자는 체크기호로 ISBN의 정확성 여부를 점검할 수 있는 숫자이다. 
# 이 체크기호는 일련번호의 앞에서부터 각 자리마다 가중치 1, 3, 1, 3…. 를 곱한 것을 모두 더하고, 
# 그 값을 10으로 나눈 나머지가 0이 되도록 만드는 숫자 m을 사용한다. 수학적으로는 다음과 같다.

# ISBN이 abcdefghijklm 일 때, a+3b+c+3d+e+3f+g+3h+i+3j+k+3l+m ≡ 0 (mod 10)

# 즉, 체크기호 m = 10 - (a+3b+c+3d+e+3f+g+3h+i+3j+k+3l) mod 10 이다.

# 단, 10으로 나눈 나머지 값이 0일 경우 체크기호는 0이다.

# 전북대학교 중앙도서관에서 사서로 일하고 있는 영훈이는 책 정리를 하다가 개구쟁이 광현이에 의해서 ISBN이 훼손된 도서들을 발견했다.0 
# 광현이때문에 야근해야 하는 불쌍한 영훈이를 위해서 손상된 자리의 숫자를 찾아내는 프로그램을 작성해주자.

# 입력
# ISBN 13자리 숫자가 입력된다. 훼손된 숫자는 *로 표시한다. (훼손된 일련번호는 체크기호를 제외한 무작위 한 자리이다.)

# 출력
# 훼손된 숫자 *에 알맞은 숫자를 출력한다.


import sys
input = sys.stdin.readline
def find_missing_digit(isbn):
    isbn = isbn.strip()
    total = 0
    missing_index = -1
    
    for i, char in enumerate(isbn):
        if char == '*':
            missing_index = i
            continue
        digit = int(char)
        if i % 2 == 0:
            total += digit
        else:
            total += 3 * digit
    
    # Calculate the expected sum modulo 10
    expected_mod = (10 - (total % 10)) % 10
    
    # Find the missing digit
    if missing_index % 2 == 0:
        return str(expected_mod)
    else:
        return str((expected_mod + 9) % 10)
    
if __name__ == "__main__":