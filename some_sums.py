n, a, b = map(int, input().split())

x = []
for i in range(n):
    s = str(i+1)
    l = list(map(int, s))
    if a <= sum(l) and sum(l) <= b:
        x.append(i+1)

print(sum(x))
