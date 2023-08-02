class Solution:
    def isPalindrome(self, x: int) -> bool:
        rev = 0
        num = x
        if( x < 0):
            return False
        while x != 0:
            rev = (rev*10) +  x % 10
            x = x // 10
        if(rev == num):
            return True
        return False
