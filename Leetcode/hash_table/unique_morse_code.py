from typing import List

"""
This is how i did but not very optimised
"""
class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        lists = [".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....", "..", ".---", "-.-", ".-..", "--", "-.",
                 "---", ".--.", "--.-", ".-.", "...", "-", "..-", "...-", ".--", "-..-", "-.--", "--.."]
        lists1 = "abcdefghijklmnopqrstuvwxyz"
        list2 = list(lists1)
        freq = {}
        for i in range(len(list2)):
            freq[list2[i]] = lists[i]
        new_list = []
        for i in range(len(words)):
            new = list(words[i])
            string = ""
            for j in range(len(words[i])):
                if new[j] in freq:
                    string = string + freq[new[j]]
            new_list.append(string)
        return len(set(new_list))

