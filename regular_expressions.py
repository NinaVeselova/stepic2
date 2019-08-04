# https://stepik.org/lesson/24470/step/11?unit=6776
import re
import sys

pattern = r'\b(\w+)\1\b'
for line in sys.stdin:
    line = line.rstrip()
    if len(re.findall(pattern, line)) > 0:
        print(line)

