class Solution:
    def isPalindrome(self, s: str) -> bool:
        def nonAlphaNumeric(char):
            # print(ord('a'), ord('A'))
            if not(ord(char) >= ord('a') and ord(char) <= ord('z')) and not(ord(char) >= ord('A') and ord(char) <= ord('Z'))  and not(ord(char) >= ord('0') and ord(char) <= ord('9')):
                return True
            return False
        
        l = 0
        r = len(s) - 1
        while l < r:
            leftChar = None
            rightChar = None
            while nonAlphaNumeric(s[l]) :
                l += 1
                if l >= len(s):
                    return True
            if ord(s[l])  >= ord('A') and ord(s[l]) <= ord('Z'):  
                leftChar = chr(ord(s[l]) + 32)
            if leftChar is None:
                leftChar = s[l]    

            while nonAlphaNumeric(s[r]):
                r -= 1    
                if r < 0:
                    return True
            if ord(s[r]) >= ord('A') and ord(s[r]) <= ord('Z'):  
                rightChar = chr(ord(s[r]) + 32)    
            if rightChar is None:
                rightChar = s[r]
            
            # print (leftChar, rightChar)
            if leftChar != rightChar:
                return False
            else:
                l += 1
                r -= 1
    
            """
            if non alphabets: ord(s[i]) < ord('A') or ord(s[i]) > ord('z')
                l+=1
            else if capital letters:
            elif ord(s[i]) is >= ord('A') and <= ord('Z'):
                then we add 26 to make it small
                    newChar = str(ord(s[i]) + 26)
            """        
                    
        return True