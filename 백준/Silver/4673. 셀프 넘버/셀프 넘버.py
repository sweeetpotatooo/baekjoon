def self_num(n):
  x = list(str(n))
  result = 0
  for i in range(len(x)):
      result += int(x[i])
  result = result + n
  return result

results = set() # 중복제거를 위해 set함수 사용
for i in range(10000):
    results.add(self_num(i))
for m in range(1,10001):
    if m not in results: # 생성자 안에 없다면 셀프넘버
        print(m)
