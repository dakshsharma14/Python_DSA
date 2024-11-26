file = open('data.txt', 'a')  # read mode file
#file.write('Hello i am daksh') overrides the data
content = '\nHello i am daksh'
file.write(content)
file.close()
