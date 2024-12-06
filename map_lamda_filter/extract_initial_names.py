names = ["Daksh Sharma", "Rantej Singh", "Rohit Sharma"]

initials = list(map(lambda name: "".join([n[0] for n in name.split()]),names))
print(initials)


# reverse a list using map
reverse = list(map(lambda names: names[::-1],names))
print(reverse)