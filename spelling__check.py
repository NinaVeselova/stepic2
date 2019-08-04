# https://stepik.org/lesson/3380/step/3?unit=963
dictionary = dict.fromkeys(input().lower() for i in range(int(input())))
text = []
for i in range(int(input())):
    text += input().lower().strip('\n').split(' ')
result = dict.fromkeys(text)
for i in dictionary.keys():
    if i in result.keys():
        result.pop(i)
for i in result.keys():
    print(i)
