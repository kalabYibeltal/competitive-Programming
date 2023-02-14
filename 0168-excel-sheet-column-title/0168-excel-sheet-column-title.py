class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        string = ''
        while columnNumber > 0:
            columnNumber -= 1
            string = chr(65 + columnNumber % 26) + string
            columnNumber = columnNumber // 26
        return string