'''
convert the string to a  list or split
list(nums)
if the list is dtring
this is very efficient that for loop and list(int(num))
new_list = list(map(int, numbers))
'''

"""
USE OF SORTED FUNCTION

words = ["apple", "bat", "cat", "elephant"]
sorted_by_length = sorted(words, key=len)
print(sorted_by_length)  # Output: ['bat', 'cat', 'apple', 'elephant']
"""

"""
lambda arguments: expression

# Normal function
def square(x):
    return x * x

# Lambda function
square_lambda = lambda x: x * x
print(square_lambda(5))  # Output: 25



data = [(1, 'B'), (2, 'A'), (3, 'C')]

# Sort by the second element (index 1)
sorted_data = sorted(data, key=lambda x: x[1])
print(sorted_data)  # Output: [(2, 'A'), (1, 'B'), (3, 'C')]
Explanation:
x represents each tuple in the list.
x[1] extracts the second element of each tuple for comparison.
sorted() arranges the tuples based on the values returned by lambda.



students = [("Alice", 25), ("Bob", 20), ("Charlie", 25)]

# Sort by age, then by name
sorted_students = sorted(students, key=lambda x: (x[1], x[0]))
print(sorted_students)  
# Output: [('Bob', 20), ('Alice', 25), ('Charlie', 25)]
Explanation:
x[1] sorts by age.
x[0] is the tie-breaker, sorting by name when ages are equal.




Complex Transformations
data = ["apple", "banana", "pear"]

# Sort by the last character in each word
sorted_by_last_char = sorted(data, key=lambda x: x[-1])
print(sorted_by_last_char)  # Output: ['banana', 'apple', 'pear']
Explanation:
x[-1] retrieves the last character of each string.
"""