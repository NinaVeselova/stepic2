# https://stepik.org/lesson/3380/step/2?unit=963
dict1 = input()
dict2 = input()
origin_string = input()
crypto_string = input()
dictionary = dict(zip(dict1,dict2))
reverse_dictionary = dict(zip(dict2,dict1))
s = ''
for i in origin_string:
    s = s + dictionary[i]
print(s)
s = ''
for i in crypto_string:
    s = s + reverse_dictionary[i]
print(s)



