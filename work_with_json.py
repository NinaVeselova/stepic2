# https://stepik.org/lesson/24473/step/4?unit=6777
import json

def children(a):
    tempo = [a]
    for k in D:
        if a in D[k]:
            tempo.extend(children(k))
    return tempo


data = json.loads(input())
dictionary = {}
for i in data:
    dictionary[i['name']] = i['parents']
parents = {}
for i in dictionary:
    parents[i] = children(i)
res = []
for key, value in parents.items():
    res.append([key, str(len(set(value)))])
res.sort()
for i in res:
    print(' : '.join(i))



