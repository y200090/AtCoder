S = input()

addList = ['dream', 'dreamer', 'erase', 'eraser']

for add in addList:
    while add in S:
        S = S.replace(add, '')

if len(S) == 0:
    print('YES')
else:
    print('NO')
