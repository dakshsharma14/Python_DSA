# alway have the prime
class HashTable:
    def __init__(self, size=7):
        self.data_map = [None] * size

    '''
    Hash Function (__hash):

The hash function is defined as a private method __hash(self, key).
It takes a key as input.
It initializes a variable my_hash to 0.
It iterates through each character in the key.
For each character, it calculates the hash using the formula (my_hash + ord(letter) * 23) % len(self.data_map), where ord(letter) returns the ASCII value of the character.
It updates my_hash with the new value.
Finally, it returns the calculated hash

Compression Function:

The compression function is implicitly defined by the modulus operation in the hash
 function.
 
The modulus operation %(len(self.data_map)) ensures that the calculated hash value
 falls within the bounds of the data map, effectively compressing it to fit within
the size of the data map.
    '''

    def __hash(self, key):
        my_hash = 0
        for letter in key:
            '''
            This formula seems to be a variation of the additive hashing method. 
            In additive hashing, you accumulate the ASCII or Unicode values of the 
            characters in the key and then perform some arithmetic operation to map 
            the result into the range of the hash table.

In this specific formula:

my_hash likely holds the current hash value.
ord(letter) gives the Unicode code point of the character letter.
23 is a constant multiplier.
% len(self.data_map) ensures that the resulting hash value falls within the range 
of the hash table (i.e., it wraps around if it exceeds the table size).'''
            my_hash = (my_hash + ord(letter) * 23) % len(self.data_map)
        return my_hash

    def print_table(self):
        for i, val in enumerate(self.data_map):
            print(i, ": ", val)


my_hash_table = HashTable()

my_hash_table.print_table()