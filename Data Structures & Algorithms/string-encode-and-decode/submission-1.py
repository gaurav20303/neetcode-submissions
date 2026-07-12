class Solution:

    def encode(self, strs: List[str]) -> str:
        ans = ''
        for s in strs:
            ans += s+'✓'
        
        #ans = ans[:-1]
        #print(ans)
        return ans

    def decode(self, s: str) -> List[str]:
        ans = []
        a = ''
        for c in s:
            print(c)
            if c != '✓':
                a += c
            else:
                ans.append(a)
                a = ''
        return ans
