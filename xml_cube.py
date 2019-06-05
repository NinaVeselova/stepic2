# https://stepik.org/lesson/24474/step/4?unit=6779
from xml.etree import ElementTree


def color_count(cube):
    global count
    colours[cube.attrib['color']] += count
    if len(cube) > 0:
        count += 1
        for child in cube:
            color_count(child)
        count -= 1


colours = {'red': 0, 'green': 0, 'blue': 0}
count = 1
tree = ElementTree.fromstring(input())
color_count(tree)
print(colours['red'], colours['green'], colours['blue'])
