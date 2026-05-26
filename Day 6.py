class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        unique_chars = set(word)
        return sum(1 for c in unique_chars if c.islower() and c.upper() in unique_chars)
