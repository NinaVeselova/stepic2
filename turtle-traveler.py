# https://stepik.org/lesson/3380/step/4?unit=963
n = int(input())
coordinates = [0,0]
for i in range(n):
    a = input().split(' ')
    if a[0] == 'север':
        coordinates[1] += int(a[1])
    elif a[0] == 'юг':
        coordinates[1] -= int(a[1])
    elif a[0] == 'восток':
        coordinates[0] += int(a[1])
    else:
        coordinates[0] -= int(a[1])
print(*coordinates, end=' ')




