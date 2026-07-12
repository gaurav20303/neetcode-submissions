class Solution:
    def climbStairs(self, n: int) -> int:
        def reach(n, m={}):
            if n == 1:
                m[1] = 1
                return 1
            if n == 2:
                m[2] = 2
                return 2
            if n in m:
                return m[n]
            m[n] = reach(n-1, m) + reach(n-2, m)
            return m[n]

        return reach(n)
        