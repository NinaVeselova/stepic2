# https://stepik.org/lesson/24466/step/5?unit=6773
import datetime
m = [int(i) for i in input().split(' ')]
date = datetime.datetime(m[0],m[1],m[2]) + datetime.timedelta(int(input()))
print(date.year, date.month, date.day)
