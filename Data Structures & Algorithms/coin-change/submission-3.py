class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        mem = {}
        def dfs(rem):
            if rem < 0:
                return amount+1
            if rem == 0:
                return 0 
            ans = amount+1

            if rem in mem:
                return mem[rem]

            for coin in coins:
                ans = min(ans, 1+dfs(rem-coin))
                mem[rem] = ans
            return ans

        res = dfs(amount)

        print(res)
        return res if res != amount+1 else -1
