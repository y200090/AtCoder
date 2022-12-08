n = int(input())
a = list(map(int, input().split()))

alice = []
bob = []

for _ in range(n):
    if not a:
        break
    else:
        alice.append(max(a))
        a.remove(max(a))
    if not a:
        break
    else:
        bob.append(max(a))
        a.remove(max(a))

result = sum(alice) - sum(bob)
print(result)
