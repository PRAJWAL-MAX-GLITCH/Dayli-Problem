class Solution:
    def maxJumps(self, arr: List[int], d: int) -> int:
        n = len(arr)
        dp = [-1] * n      
        def dfs(i):
            if dp[i] != -1:
                return dp[i]          
            ans = 1
            for j in range(i - 1, max(i - d - 1, -1), -1):
                if arr[i] > arr[j]:
                    ans = max(ans, 1 + dfs(j))
                else:
                    break
            for j in range(i + 1, min(i + d + 1, n)):
                if arr[i] > arr[j]:
                    ans = max(ans, 1 + dfs(j))
                else:
                    break           
            dp[i] = ans
            return ans       
        return max(dfs(i) for i in range(n))