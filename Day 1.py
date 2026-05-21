class Solution:
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
        prefix_set = set()
        for num in arr1:
            s = str(num)
            for i in range(1, len(s)+1):
                prefix_set.add(s[:i])       
        max_len = 0
        for num in arr2:
            s = str(num)
            for i in range(1, len(s)+1):
                if s[:i] in prefix_set:
                    max_len = max(max_len, i)        
        return max_len