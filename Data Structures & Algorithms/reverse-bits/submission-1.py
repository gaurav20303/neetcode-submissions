class Solution:
    def reverseBits(self, n: int) -> int:
        res = 0

        # for i in range(32):
        #     b = (n >> i) & 1
        #     if b:
        #         res |= 1 << (31-i)


        for i in range(32):
            b = n & 1
            print(b)
            n = n >> 1
            res = res | b << (31-i)


        return res