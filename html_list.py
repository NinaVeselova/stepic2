# https://stepik.org/lesson/24471/step/7?unit=6780
import re
import requests

content = requests.get(input()).text
pattern = r'<a.*?href=".*?:\/\/((?:\w|-)+(?:\.(?:\w|-)+)+)'
urls = re.findall(pattern, content)
result = list(set(urls))
result.sort()
print('\n'.join(result))