class Solution:
    def myAtoi(self, s: str) -> int:
        i = 0
        n = len(s)
        ans = 0
        sign = 1
        
        # 1. Skip leading whitespace
        while i < n and s[i] == " ":
            i += 1
            
        # 2. Check for sign
        if i < n and (s[i] == "+" or s[i] == "-"):
            if s[i] == "-":
                sign = -1
            i += 1
            
        # 3. Read digits
        while i < n and s[i].isdigit():
            ans = ans * 10 + int(s[i])
            i += 1
            
        ans *= sign
        
        # 4. Clamp to 32-bit signed integer range [-2^31, 2^31 - 1]
        INT_MIN = -2**31
        INT_MAX = 2**31 - 1
        
        if ans < INT_MIN:
            return INT_MIN
        if ans > INT_MAX:
            return INT_MAX
            
        return ans