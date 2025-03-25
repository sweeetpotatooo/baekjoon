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
