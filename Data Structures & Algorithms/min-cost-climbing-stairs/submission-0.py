class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        
        def reach(n, m={}):
            if n == 0:
                m[0] = 0
                return 0

            if n == 1:
                m[1] = 0
                return 0
            if n in m:
                return m[n]
            m[n] = min(cost[n-1]+reach(n-1, m), cost[n-2]+reach(n-2, m))
            return m[n]
        
        return reach(len(cost))