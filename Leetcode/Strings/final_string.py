"""
Instead, we can use a list to collect the characters and then join them at the end, which is much faster for large strings.
"""
class Solution:
    def finalString(self, s: str) -> str:
        chars = []
        for char in s:
            if char == "i":
                chars.reverse()
            else:
                chars.append(char)
        return ''.join(chars)
"""
class Solution:
    def finalString(self, s: str) -> str:
        strings = ""
        for i in range(len(s)):
            if s[i] == "i":
                strings = strings[::-1]
            else:
                strings += s[i]
        return strings
        
"""