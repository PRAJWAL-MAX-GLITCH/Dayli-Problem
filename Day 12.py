class Solution:
    def minimumCost(self, cost: list[int]) -> int:
        cost.sort()
        total_cost = 0
        for i in range(len(cost) -1, -1, -3):
            total_cost += cost[i]
            if i - 1 >= 0:
                total_cost += cost[i - 1]
        return total_cost
