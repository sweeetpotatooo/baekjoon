L = int(input())
S = input().strip()
r = 31
M = 1234567891
hash_value = 0
for i in range(L):
    hash_value += (ord(S[i]) - ord('a') + 1) * pow(r, i, M)
    hash_value %= M
print(hash_value)