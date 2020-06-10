string = ['a', 'b', 'c', 'd']

print(string[2])  # prints the letter in second index

# push
string.append('e')  # O(1)

print(string)  # adds 'e' to the end

# pop
string.pop()  # O(1)

print(string)

# add first element
string.insert(0, 'x')  # O(n)

print(string)  # adds 'x' to the index of 0

# splice
string.insert(2, 'alien')  # O(n)

print(string)
