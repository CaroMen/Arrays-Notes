a = [1, 2, 3, 4, 6, 20]
b = [2, 3, 4, 5, 6, 9, 11, 76]


def merge(a, b):
    if len(a) == 0 or len(b) == 0:
        return a + b

    list = []
    n = 0
    m = 0
    while n < len(a) and m < len(b):

        if a[n] <= b[m]:
            list.append(a[n])
            n += 1
        elif b[m] < a[n]:
            list.append(b[m])
            n += 1

    return list + a[n:] + b[m:]


x = merge(a, b)
print(x)
