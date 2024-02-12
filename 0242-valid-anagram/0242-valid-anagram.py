class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        len_s = len(s)
        len_t = len(t)
        if len_s != len_t:
            return False
        map_s = {}
        for char in s:
            if char in map_s:
                map_s[char] += 1
            else:
                map_s[char] = 1
        
        for char in t:
            if char not in map_s:
                return False
            if map_s[char] == 0:
                return False
            else:
                map_s[char] -= 1
        
        return True