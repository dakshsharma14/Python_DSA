import re


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