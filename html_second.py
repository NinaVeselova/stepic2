# https://stepik.org/lesson/24471/step/6?unit=6780
import requests
import lxml.html as html
import re

first = input()
second = input()
res = requests.get(first)
urls = re.findall(r'href="(.*)"', res.text)
candidates = []
for i in urls:
    a = requests.get(i)
    candidates.extend(re.findall(r'href="(.*)"', a.text))
if second in candidates:
    print("Yes")
else:
    print('No')
