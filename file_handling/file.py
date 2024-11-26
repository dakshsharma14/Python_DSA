file = open('data.txt', 'r')  # read mode file
content = file.read(10) # reads bytes
# content = file.readline() first line
print(content)
file.close()
