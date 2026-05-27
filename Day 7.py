class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        lower = set()
        upper = set()
        for c in word:
            if c.islower():
                lower.add(c)
            else:
                upper.add(c)
        count = 0
        for c in lower:
            if c.upper() in upper and word.rindex(c) < word.index(c.upper()):
                count += 1
        return count
