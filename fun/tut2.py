
even = []


def evenfun(num):
    for i in num:
        if i % 2 == 0:
            even.append(i)

    return even


# print(evenfun([10, 4, 3, 5, 7, 2, 12]))
