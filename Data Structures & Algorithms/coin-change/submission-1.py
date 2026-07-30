class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = {}

        def dfs(remain):
            if remain == 0:
                return 0

            if remain < 0:
                return float('inf')

            if remain in memo:
                return memo[remain]

            ans = float('inf')

            for coin in coins:
                ans = min(ans, 1 + dfs(remain - coin))

            memo[remain] = ans
            return ans

        ans = dfs(amount)
        return ans if ans != float('inf') else -1

            