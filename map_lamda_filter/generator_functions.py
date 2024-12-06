def function():
    counter = 0
    while counter <=10:
        yield counter
        counter = counter +1
print(list(function()))

def even_generator(s):
    for i in range(s):
        if i%2 ==0:
            yield i

print(list(even_generator(10)))