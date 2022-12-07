a = int(input())
b, c = (int(x) for x in input().split())
# b, c = map(int, input().split())
s = input()

sum = a + b + c
print(f'{sum} {s}')
