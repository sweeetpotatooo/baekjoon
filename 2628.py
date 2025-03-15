rec_w, rec_h = map(int, input().split())
num_line = int(input())

cut_w = [0, rec_w]
cut_h = [0, rec_h]

for _ in range(num_line):
    w_or_h, line = map(int, input().split())
    if w_or_h == 0:
        cut_h.append(line)  
    else:
        cut_w.append(line) 

cut_w.sort()
cut_h.sort()

max_w = max(cut_w[i] - cut_w[i - 1] for i in range(1, len(cut_w)))
max_h = max(cut_h[i] - cut_h[i - 1] for i in range(1, len(cut_h)))

print(max_w * max_h)
