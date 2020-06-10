def reverse(string):
    list = []
    for letter in range(len(string) - 1, -1, -1):
        list.append(string[letter])
    return ''.join(list)


x = reverse('I am caro')
print(x)
