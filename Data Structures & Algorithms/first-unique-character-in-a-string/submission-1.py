class Solution:
    def firstUniqChar(self, s: str) -> int:
        freq = {}

        # Count frequencies
        for ch in s:
            freq[ch] = freq.get(ch, 0) + 1

        # Find first unique character
        for i, ch in enumerate(s):
            if freq[ch] == 1:
                return i

        return -1

        
        