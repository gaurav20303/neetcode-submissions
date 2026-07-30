class Solution:
    def compress(self, chars: List[str]) -> int:
        write = 0
        i = 0
        n = len(chars)

        while i < n:
            char = chars[i]
            count = 0
            while i < n and chars[i] == char:
                count += 1
                i += 1

            chars[write] = char
            write += 1

            if count > 1:
                l = str(count)
                for c in l:
                    chars[write] = c
                    write += 1

        return write