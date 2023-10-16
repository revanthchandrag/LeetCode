class Solution:
    def romanToInt(self, s: str) -> int:
        integer = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        int_val = 0
        
        for i in range(len(s)):
            if i == len(s)-1:
                int_val += integer[s[i]]
            elif integer[s[i]] < integer[s[i+1]]:
                int_val -= integer[s[i]]
            else:
                int_val += integer[s[i]]
        return int_val    