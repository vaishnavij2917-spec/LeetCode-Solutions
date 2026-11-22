class Solution:
    def reverse(self, x: int) -> int:
        flag=False
        if x<0:
            x=x*-1
            flag=True
        s=0
        while(x!=0):
            r=x%10
            s=s*10+r
            x=x//10
        if s>2**31-1:
            return 0
        if flag==True:
            return s*-1
        else:
            return s


        