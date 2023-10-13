class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        columnNumber = 0
        j = 0
        for i in range(len(columnTitle)-1 , -1, -1):
            val = ord(columnTitle[i]) - ord('A') + 1
            columnNumber += val * (26 ** j)
            j += 1
            
        return columnNumber 