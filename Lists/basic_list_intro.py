# list slicing, during this it will make a new list

# big O of this is O(k) k is the size of the resulting slice
car = [
    'hey',
    'how',
    'are',
    'fruits',
    'heyyyyy'
]

print(car[0::3])  # O(k) k is the size of the resulting slice that is O(2)

# below list will make O(3) constant time, as final list will have 3 elements

car2 = [
    'hey',
    'how',
    'are',
    'fruits',
    'heyyyyy'
]

print(car2[0:5:2])

# how to copy a list using list slicing

car2[0] = 'laptop'
new_car = car2[:]
# or .copy()

new_car[0] = 'gum'

print(car2)
print(new_car)

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [0, 1, 0]
]

lis = [1, 2, 3, 4, 5, 9, 7, 9]
lis.insert(3, 23)  # O(n)
lis.extend([112])
print(lis)

lis.pop()  # O(1)
print(lis)
lis.remove(3)

lis.index(2)  # gives what index is 2 at


lis2 = [1, 2, 3, 4, 5, 9, 7, 9]
print(lis2.count(9))

lis2.sort()
lis2.reverse()
print(lis2[::-1])  # this creates a new list
print(lis2)

# creating a list
print(list(range(1, 100)))

sentence = ' '
new_sentence = sentence.join(['hi', 'my', 'is', 'Daksh'])
print(new_sentence)

# list unpacking
a, b, c, *other = [1, 2, 3, 4, 5, 6]
