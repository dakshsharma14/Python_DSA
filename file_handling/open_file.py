with open('data.txt', 'r') as file:
    content = file.read()
    print(content)

with open('data.txt', 'r') as file:
    line1 = file.readline()
    # print(content)
print(line1)

with open('data.txt', 'r') as file:
    lines = file.readlines()
    # print(content)
print(lines)



for line in lines:
    print(line)

