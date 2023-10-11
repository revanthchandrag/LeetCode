class Solution:
    def isValid(self, s: str) -> bool:
        arr = []
        for char in s:
            if char == '(' or char == '[' or char == '{':
                arr.append(char)
            else:
                if arr != []:
                    char2 = arr.pop()
                else:
                    return False
                # print(char, char2)
                if char == ')':
                    # char2 = arr.pop()
                    if char2 != '(':
                        return False
                elif char == ']':
                    # char2 = arr.pop()
                    if char2 != '[':
                        return False
                else:
                    if char2 != '{':
                        return False
        print(arr)
        if arr == []:     
            return True        
        else:
            return False