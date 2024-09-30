class Solution:
    def evaluate(self, s: str, knowledge: list[list[str]]) -> str:
        # Create a dictionary from knowledge for quick lookup
        knowledge_dict = dict(knowledge)

        result = []
        key = []
        inside_bracket = False

        # Iterate through the string character by character
        for char in s:
            if char == '(':
                inside_bracket = True
                key = []  # Start collecting key characters
            elif char == ')':
                inside_bracket = False
                # Lookup the key and append its value or "?" if key not found
                result.append(knowledge_dict.get(''.join(key), '?'))
            elif inside_bracket:
                key.append(char)  # Collect characters inside the brackets
            else:
                result.append(char)  # Add characters outside the brackets

        return ''.join(result)