class Solution:
    def isAlphaNumeric(self, ch):
        number = ord(ch) > 47 and ord(ch) < 58
        lowerchar = ord(ch) > 64 and ord(ch) < 91
        upperchar = ord(ch) > 96 and ord(ch) < 123
        if number or lowerchar or upperchar:
            return True
        return False

    def isPalindrome(self, s: str) -> bool:
        n = len(s)
        i = 0
        j = n-1
        while i < j:
            if not self.isAlphaNumeric(s[i]):
                i += 1
                continue

            if not self.isAlphaNumeric(s[j]):
                j -= 1
                continue

            if s[i].lower() != s[j].lower():
                return False
            i += 1
            j -= 1
        return True
        