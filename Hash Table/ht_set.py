class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [[] for _ in range(size)]

    def _hash(self, key):
        return key % self.size  # Simple hash function using modulo operation

    def insert(self, key, value):
        index = self._hash(key)
        self.table[index].append([key, value])

    def get(self, key):
        index = self._hash(key)
        for k, v in self.table[index]:
            if k == key:
                return v
        return None  # Key not found

# Let's create two hash tables, one with a prime size and one without
prime_size_table = HashTable(11)  # Prime number size
regular_size_table = HashTable(10)  # Non-prime number size

# Insert some key-value pairs into both tables
for i in range(20):
    prime_size_table.insert(i, f"value_{i}")
    regular_size_table.insert(i, f"value_{i}")

# Now let's compare the distribution of keys in both tables
print("Prime Size Table:")
for index, bucket in enumerate(prime_size_table.table):
    print(f"Index {index}: {len(bucket)} items")

print("\nRegular Size Table:")
for index, bucket in enumerate(regular_size_table.table):
    print(f"Index {index}: {len(bucket)} items")
