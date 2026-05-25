from collections import deque

class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        n = len(s)
        queue = deque([0])
        far = 0
        while queue:
            i = queue.popleft()
            start = max(i + minJump, far + 1)
            end = min(i + maxJump, n - 1)
            for j in range(start, end + 1):
                if s[j] == '0':
                    if j == n - 1:
                        return True
                    queue.append(j)
            far = end
        return n == 1
