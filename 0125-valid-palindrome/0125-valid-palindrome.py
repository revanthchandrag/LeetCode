class Solution:
    def isPalindrome(self, s: str) -> bool:
        def isAlphanumeric(char):
            return char.isalnum()  # Check if a character is alphanumeric
        
        l = 0
        r = len(s) - 1
        
        while l < r:
            while l < r and not isAlphanumeric(s[l]):
                l += 1
            while l < r and not isAlphanumeric(s[r]):
                r -= 1
            
            leftChar = s[l].lower()  # Convert to lowercase
            rightChar = s[r].lower()
            
            if leftChar != rightChar:
                return False
            
            l += 1
            r -= 1
        
        return True
