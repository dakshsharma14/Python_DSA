# below this I will talk about the O(n2)

num = [1, 2, 3]
for i in range(len(num)):
    for j in range(i+1, len(num)):
        print(num[i],num[j])

