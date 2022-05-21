
import re


even = []


def evenfun(num):
    for i in num:
        if i % 2 == 0:
            even.append(i)

    return even


odd = []


def oddfun(num):
    for i in num:
        if i % 2 != 0:
            odd.append(i)
    return odd


# print(evenfun([10, 4, 3, 5, 7, 2, 12]))
# print(oddfun([10, 4, 3, 5, 7, 2, 12]))
