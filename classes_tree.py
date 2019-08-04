# https://stepik.org/lesson/24462/step/7?unit=6768
def is_class_root(class1, class2):
    global flag
    if class1 == class2:
        flag = flag + 1
        return
    if dictionary.get(class2) is None:
        return
    if dictionary[class2] != []:
        if class1 in dictionary[class2]:
            flag = flag + 1
            return
        else:
            for i in dictionary[class2]:
                is_class_root(class1, i)
    return


dictionary = {}
for i in range(int(input())):
    temp = input().replace(' : ',' ').split(' ')
    dictionary[temp[0]] = temp[1:]
for i in range(int(input())):
    temp = input().split(' ')
    flag = 0
    is_class_root(temp[0], temp[1])
    if flag > 0:
        print('Yes')
    else:
        print('No')
