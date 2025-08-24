'''
Problem

Given an integer columnNumber, return its corresponding column title as it appears in an Excel sheet.

Examples:
Input: 1
Output: "A"

Input: 28
Output: "AB"

Input: 701
Output: "ZY"

'''

def convertToTitle(self, columnNumber: int) -> str:
        result = []
        
        while columnNumber > 0:
            columnNumber -= 1  # adjust for 1-indexing
            remainder = columnNumber % 26
            result.append(chr(ord('A') + remainder))
            columnNumber //= 26
        
        # reverse because we build characters from last to first
        return ''.join(reversed(result))
'''
hello...
'''
