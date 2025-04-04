t= int(input())
for i in range(t):
    a=input()
    score=0
    sum=0
    for j in a:
        if j=='O':
            score+=1
            sum+=score
        else:
            score=0
    print(sum)
    