class Solution:
    def isValid(self, s: str) -> bool:
        maps = {")": "(", "]": "[", "}": "{"}
        stack = []

        # Iterate through each character in the string
        for char in s:
            if char in "([{":  # If it's an opening bracket, push it to the stack
                stack.append(char)
            elif char in ")]}":  # If it's a closing bracket
                if stack and stack[-1] == maps[char]:  # Check for matching opening bracket
                    stack.pop()
                else:  # Either stack is empty or brackets don't match
                    return False

        # If stack is empty at the end, all brackets were matched
        return not stack

# space worst case (e.g., s = "(((([[{{"), all characters could be opening brackets, so the stack would store all n
# characters.
# Thus, the space used by the stack is O(n).
