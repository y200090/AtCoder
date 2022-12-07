n = int(input())
a = list(map(int, input().split()))
s = 0

flag = True
for b in a:
    if b % 2 != 0:
        flag = False
        print(s)
        exit()

if flag:
    while True:
        for i, x in enumerate(a):
            x = x / 2
            if x % 2 != 0:
                flag = False
            a[i] = x
        s += 1
        if flag == False:
            print(s)
            break
