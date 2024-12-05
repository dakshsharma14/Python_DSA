numbers = [1, 3, 5, 7, 9, 10]


def square(x):
    return x * x


new_list = list(map(square, numbers))
print(new_list)



#### lambda demo

lambda_test = (lambda x,y: x**2+y)(2,4)
print(lambda_test)