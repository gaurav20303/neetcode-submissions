class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_map = {}
        for word in strs:
            m = [0]*26
            #print(m)
            for char in word:
                m[ord(char)-ord('a')] += 1
            print(m)
            if tuple(m) in anagram_map:
                anagram_map[tuple(m)].append(word)
            else:
                anagram_map[tuple(m)] = [word]

        return list(anagram_map.values())


        