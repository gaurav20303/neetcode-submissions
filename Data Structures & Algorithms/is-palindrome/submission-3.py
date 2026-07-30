class Solution:
    def isPalindrome(self, s: str) -> bool:
        f_str = ""
        for i in s:
            if 48 <= ord(i) <=57 or 65 <= ord(i) <= 90 or 97 <= ord(i) <= 122:
                if 65 <= ord(i) <= 90:
                    f_str += chr(ord(i)+32)
                else:
                    f_str += i

        i = 0
        j = len(f_str)-1
        while i < j:
            if f_str[i] != f_str[j]:
                return False
            i += 1
            j -= 1
        
        return True
        