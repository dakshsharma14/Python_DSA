from typing import List


class Solution:
    def countWords(self, words1: List[str], words2: List[str]) -> int:
        count=0

        for i in words1:
            if words1.count(i)==1 and words2.count(i)==1:
                count=count+1

        return count


    """
    or
    class Solution:
    def countWords(self, words1: List[str], words2: List[str]) -> int:
        freq1 = Counter(words1)
        freq2 = Counter(words2)
        freq_count1 = 0
        for i in words1:
            if (freq1[i] == 1) and (i in words2) and (freq2[i] == 1):
                freq_count1 +=1
        return freq_count1
        
    """