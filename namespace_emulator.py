# https://stepik.org/lesson/24460/step/9?unit=6766
env = {'global' : [[], []]}


def get (space, var):
    if var in env[space][0]:
        return space
    elif space == 'global' and var not in env[space][0]:
        return 'None'
    else:
        return get(env[space][1],var)


n = int(input())
for i in range(n):
    cmd, space, var = input().split(' ')
    if cmd == 'add':
       env[space][0].append(var)
    elif cmd == 'create':
        env[space] = [[], var]
    else:
        print(get(space,var))

