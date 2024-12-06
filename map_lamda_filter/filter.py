numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
odd_num = []
for num in numbers:
    if num % 2 == 1:
        odd_num.append(num)

print(odd_num)


def odd(x):
    if x % 2 == 1:
        return x


# filter is  a boolean function
odd_number = list(filter(odd, numbers))

# or list(filter(lamda x : x%2==1, numbers))
print(odd_number)
