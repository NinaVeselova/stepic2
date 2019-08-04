# https://stepik.org/lesson/24469/step/6?unit=6775
s, a, b, n = input(), input(), input(), 0
while n < 1001:
    if s.find(a) == -1:
        break
    else:
        n += 1
        s = s.replace(a, b)
if n != 1001:
    print(n)
else:
    print('Impossible')
