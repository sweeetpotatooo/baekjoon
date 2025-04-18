def is_prime(n):
    if n <= 1:
        return False
    for j in range(2, n + 1):
        if n % j == 0:
            if n == j:
                return True
            return False

n = int(input()) # 테스트 케이스 수

for i in range(n):
    num = int(input())
    prime1, prime2 = num//2 , num//2
    while prime1 > 0:
        if is_prime(prime1) and is_prime(prime2):
            print (prime1, prime2)
            break
        else:
            prime1= prime1-1
            prime2= prime2+1
