import re
'''
Found online better with memory as it is not creating result and taking up the extra memory
class Solution:
    def isPalindrome(self, s: str) -> bool:
        first, last = 0, len(s) - 1
        while first < last:
            # Skip non-alphanumeric characters
            while first < last and not s[first].isalnum():
                first += 1
            while first < last and not s[last].isalnum():
                last -= 1
            # Compare characters
            if s[first].lower() != s[last].lower():
                return False
            first += 1
            last -= 1
        return True
        
my implementation 
class Solution:
    def isPalindrome(self, s: str) -> bool:
        result = ''.join(c.lower() for c in s if c.isalnum())
        first, last = 0, len(result)-1
        while first < last:
            if result[first] != result[last]:
                return False
            first +=1
            last -=1
        return True
        
'''

class Solution:
    def isPalindrome(self, s: str) -> bool:
        # Filter out non-alphanumeric characters and convert to lowercase
        filtered_string = re.sub(r'[^a-zA-Z0-9]', '', s).lower()

        # Initialize pointers for the start and end of the string
        start, end = 0, len(filtered_string) - 1

        # Check for palindrome by comparing characters from both ends
        while start < end:
            if filtered_string[start] != filtered_string[end]:
                return False
            start += 1
            end -= 1

        return True
"""
isalum(): this will check it is alfanumerice
class Solution:
    def isPalindrome(self, s: str) -> bool:
        l = 0
        r = len(s) - 1
        while l < r:
            if not s[l].isalnum():
                l += 1
            elif not s[r].isalnum():
                r -= 1
            elif s[l].lower() == s[r].lower():
                l += 1
                r -= 1
            else:
                return False

        return True
"""