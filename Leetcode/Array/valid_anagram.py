from collections import Counter


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # below has complexity of O(nlogn)
        # s1 = ''.join(sorted(s))
        # t1 = ''.join(sorted(t))
        # if s1 == t1:
        #     return True
        # else:
        #     return False

        # below O(n)
        """
        from collections import Counter

        # Example with a string
        s = "anagram"
        counter_s = Counter(s)

        print(counter_s)

        Counter({'a': 3, 'n': 1, 'g': 1, 'r': 1, 'm': 1})


        """
        return Counter(s) == Counter(t)
