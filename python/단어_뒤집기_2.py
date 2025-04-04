# 문자열 S가 주어졌을 때, 이 문자열에서 단어만 뒤집으려고 한다.
# 먼저, 문자열 S는 아래와과 같은 규칙을 지킨다.

# 알파벳 소문자('a'-'z'), 숫자('0'-'9'), 공백(' '), 특수 문자('<', '>')로만 이루어져 있다.
# 문자열의 시작과 끝은 공백이 아니다.
# '<'와 '>'가 문자열에 있는 경우 번갈아가면서 등장하며, '<'이 먼저 등장한다. 또, 두 문자의 개수는 같다.
# 태그는 '<'로 시작해서 '>'로 끝나는 길이가 3 이상인 부분 문자열이고, '<'와 '>' 사이에는 알파벳 소문자와 공백만 있다. 단어는 알파벳 소문자와 숫자로 이루어진 부분 문자열이고, 연속하는 두 단어는 공백 하나로 구분한다. 태그는 단어가 아니며, 태그와 단어 사이에는 공백이 없다.

# 입력
# 첫째 줄에 문자열 S가 주어진다. S의 길이는 100,000 이하이다.

# 출력
# 첫째 줄에 문자열 S의 단어를 뒤집어서 출력한다.

def reverse_words_in_tags(sentence):
    answer = []
    stack = []
    inside_tag = False
    
    for ch in sentence:
        if ch == '<':
            # 태그 시작 전까지 쌓인 것(단어들)을 뒤집어서 결과에 추가
            while stack:
                answer.append(stack.pop())
            
            inside_tag = True
            answer.append(ch)  # '<' 자체를 결과에 추가
            
        elif ch == '>':
            inside_tag = False
            answer.append(ch)  # '>' 자체를 결과에 추가
            
        else:
            if inside_tag:
                # 태그 내부는 그대로 추가
                answer.append(ch)
            else:
                # 태그 밖의 문자
                if ch == ' ':
                    # 스택에 쌓인 문자(단어)를 모두 뒤집어서 결과에 추가
                    while stack:
                        answer.append(stack.pop())
                    # 공백은 그대로 추가
                    answer.append(ch)
                else:
                    # 단어(알파벳/숫자)를 스택에 쌓음
                    stack.append(ch)
    
    # 반복문이 끝나고 스택에 남은 내용이 있다면(마지막 단어) 뒤집어 추가
    while stack:
        answer.append(stack.pop())
    
    return "".join(answer)

# 테스트
if __name__ == "__main__":
    sentence = input().rstrip()
    print(reverse_words_in_tags(sentence))
