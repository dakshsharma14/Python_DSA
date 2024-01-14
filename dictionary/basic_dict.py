#  it is a data structure, unordered(inside memory) key value pair
dicti = {
    'a': 2,
    'b': 3,
    'c': 'Hello'
}

print(dicti['a'], dicti['c'])

print(dicti.items())


# best way to retrieve
print(dicti.get('c'))

# to retrieve, but if that exist then good, otherwise give them random output so
# if it doesn't have any value then generate that
print(dicti.get('d', 66))

# dic inside the list
my_list = [
    {
        'a': 2,
        'b': 3,
        'c': 'Hello'
    },
    {
        'e': 8,
        'f': [4, 5, 6],
        'g': 'Hey'
    }

]

print(my_list[1]['f'][0])

# creating key value pair
user2 = dict(name='Daksh')
print(user2)