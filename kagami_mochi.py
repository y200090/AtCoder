n = int(input())
d = []
for i in range(n):
    d.append(int(input()))

d = len(set(d))
print(d)
