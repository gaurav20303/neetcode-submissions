class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        prefix_max = [0] * n
        curr_max = height[0]
        for h in range(1,n):
            prefix_max[h] = curr_max
            if height[h] > curr_max:
                curr_max = height[h]

        print(prefix_max)

        suffix_max = [0] * n
        curr_max = height[-1]
        for h in range(n-2,-1, -1):
            suffix_max[h] = curr_max
            if height[h] > curr_max:
                curr_max = height[h]

        print(suffix_max)

        water = 0
        for i in range(n):
            w = min(prefix_max[i], suffix_max[i]) - height[i]
            if w < 0:
                w = 0
            water += w

        return water
            
