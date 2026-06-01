from typing import List
import bisect
class SegmentTree:
    def __init__(self, n):
        self.n = n
        self.tree = [0] * (4 * n)
    def update(self, idx, val, node=1, l=0, r=None):
        if r is None:
            r = self.n - 1
        if l == r:
            self.tree[node] = val
            return
        mid = (l + r) // 2
        if idx <= mid:
            self.update(idx, val, node * 2, l, mid)
        else:
            self.update(idx, val, node * 2 + 1, mid + 1, r)
        self.tree[node] = max(
            self.tree[node * 2],
            self.tree[node * 2 + 1]
        )
    def query(self, ql, qr, node=1, l=0, r=None):
        if r is None:
            r = self.n - 1
        if qr < l or ql > r:
            return 0
        if ql <= l and r <= qr:
            return self.tree[node]
        mid = (l + r) // 2
        return max(
            self.query(ql, qr, node * 2, l, mid),
            self.query(ql, qr, node * 2 + 1, mid + 1, r)
        )
class Solution:
    def getResults(self, queries: List[List[int]]) -> List[bool]:
        MAXX = max(q[1] for q in queries) + 1
        seg = SegmentTree(MAXX + 1)
        obstacles = [0, MAXX]
        seg.update(MAXX, MAXX)
        ans = []
        for q in queries:
            if q[0] == 1:
                x = q[1]
                idx = bisect.bisect_left(obstacles, x)
                left = obstacles[idx - 1]
                right = obstacles[idx]
                obstacles.insert(idx, x)
                seg.update(right, right - x)
                seg.update(x, x - left)
            else:
                x, sz = q[1], q[2]
                best_gap = seg.query(0, x)
                idx = bisect.bisect_right(obstacles, x) - 1
                left = obstacles[idx]
                tail_gap = x - left
                ans.append(max(best_gap, tail_gap) >= sz)
        return ans