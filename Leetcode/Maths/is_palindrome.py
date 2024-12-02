class Solution:
    def isPalindrome(self, x: int) -> bool:
        #negative numebr cannot be a palindrome
        if x < 0:
            return False
        x_str = str(x)
        first, last = 0, len(x_str) - 1
        while first < last:
            if x_str[first] != x_str[last]:
                return False
            first += 1
            last -= 1
        return True