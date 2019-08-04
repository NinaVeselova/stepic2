# https://stepik.org/lesson/3369/step/10?unit=952
origin = []
x = input()
while x != 'end':
    origin.append([int(i) for i in x.split( )])
    x = input()
origin.insert(0,origin[len(origin)-1].copy())
origin.insert(len(origin),origin[1].copy())
n = len(origin)
origin[0].insert(0,0)
origin[0].append(0)
origin[n-1].insert(0,0)
origin[n-1].append(0)
m = len(origin[0])
for i in range(1,n-1):
    origin[i].append(origin[i][0])
    origin[i].insert(0,origin[i][m-3])
result = [[0 for j in range(m-2)] for i in range(n-2)]
for i in range(n-2):
    for j in range(m-2):
        result[i][j] = origin[i][j + 1] + origin[i + 1][j + 2] + origin[i + 2][j + 1] + origin[i + 1][j]
for i in range(n-2):
    for j in range(m-2):
        print(result[i][j], end = ' ')
    print()
