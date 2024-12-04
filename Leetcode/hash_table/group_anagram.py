from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram = {}

        for s in strs:
            key = "".join(sorted(s))
            if key not in anagram:
                anagram[key] = []
            anagram[key].append(s)
        return list(anagram.values())


"""
Time Complexity

	1.	Sorting Each String:
	•	For each string s in strs, you sort it to create a key. Sorting a string of length  k  takes  O(k log k) .
	•	If there are  n  strings in the list, the total cost of sorting is:

O(n  k log k)

where  k  is the average length of the strings.
	2.	Hash Map Operations:
	•	For each string, inserting into or checking the hash map is  O(1)  on average. This step takes  O(n)  in total.

Overall Time Complexity:


O(n k log k)


Space Complexity

	1.	Hash Map Storage:
	•	The hash map stores each string in its corresponding anagram group. In the worst case, all strings are unique and stored in separate keys. This takes:

O(n k)

where  n  is the number of strings and  k  is the average length of each string.
	2.	Sorted Key Creation:
	•	Each string is sorted to create the key, which requires additional temporary space for 
	the sorted string. However, since this space is reused for each string, it does not scale with  n .

Overall Space Complexity:


O(n k)

"""
