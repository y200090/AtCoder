s = input()
s1 = s[0]
s2 = s[1]
s3 = s[2]

flag = 0

if s1 == '1':
    flag += 1

if s2 == '1':
    flag += 1

if s3 == '1':
    flag += 1

print(flag)
