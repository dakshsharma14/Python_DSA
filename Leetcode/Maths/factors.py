class Solution:
    def commonFactors(self, a: int, b: int) -> int:
        new = []
        for i in range(1, a + 1):
            if a % i == 0:
                new.append(i)
        new1 = []
        for i in range(1, b + 1):
            if b % i == 0:
                new1.append(i)

        print(new, new1)
        return 1
    commonFactors(12,4)

