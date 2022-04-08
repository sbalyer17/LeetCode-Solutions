class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        
        if x < 0:
            return False

        copy_x = x

        lastDigitCount = -1
        digitCount = getDigitCount(x)
        
        while True:
            
            if digitCount == 0:
                return True

            if lastDigitCount > 0:
                
                if lastDigitCount - digitCount != 2: 
                    return False
                
            if not digitCount//2 > 0:
                return True
            
            v1 = copy_x % 10
            v2 = copy_x //(10**(digitCount-1))
           
            if v1 != v2:
                return False

            copy_x -= v2 * (10**(digitCount-1)) + v1
            copy_x //= 10
            lastDigitCount = digitCount
            digitCount -= 2


        return True  

def getDigitCount(x):
        digitCount = 1

        while x >= 10:
            x //= 10
            digitCount+=1

        return digitCount     


        # return str(x) == str(x)[::-1]
