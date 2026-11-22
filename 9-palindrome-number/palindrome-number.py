class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x<0:
            return False
        
        temp=x
        s=0
        while(x!=0):
            r=x%10
            s=s*10+r
            x=x//10
        if temp==s:
            return True
        else:
            return False
