class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        valDict = {'I': 1,
                   'V': 5,
                   'X': 10,
                   'L': 50,
                   'C': 100,
                   'D': 500,
                   'M': 1000}
        number = 0
        
        
        for index, val in enumerate(s):
            if index + 1 != len(s):
                if (valDict[val] < valDict[s[index+1]]):
                    number -= valDict[val]
                else:
                    number += valDict[val]
            else:
                number += valDict[val]
        
        return number
