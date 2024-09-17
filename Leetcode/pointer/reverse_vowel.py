class Solution:
    def reverseVowels(self, s: str) -> str:
        # Replaced lists with vowels as a set: Sets provide faster membership checking.
        vowels = set("aeiou")  # Use a set for faster look-up
        start = 0
        end = len(s) - 1
        simple_string = list(s)

        while start < end:
            while start < end and simple_string[start].lower() not in vowels:
                start += 1
            while start < end and simple_string[end].lower() not in vowels:
                end -= 1

            if start < end:
                # Swap vowels
                simple_string[start], simple_string[end] = simple_string[end], simple_string[start]
                start += 1
                end -= 1

        return "".join(simple_string)