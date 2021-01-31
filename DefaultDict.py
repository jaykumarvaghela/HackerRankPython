from collections import defaultdict

d = defaultdict(list)
n, m = input().split()
for i in range(1, (int(n) + 1)):
    d[input()].append(str(i))

lst = []
for i in range(int(m)):
    t = input()
    lst.append(' '.join(d[t])) if t in d else lst.append(-1)

for i in lst:print(i)
