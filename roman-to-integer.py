class Solution:
    def romanToInt(self, s: str) -> int:
        # using dictionary 
        singdoubles= {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000, 'CM':900, 'CD':400, 'XC':90, 'XL':40, 'IX':9, 'IV':4}
        result =0
        i = 0
        while i < len(s):
         if i+1<len(s) and s[i:i+2] in singdoubles:
            result+=singdoubles[s[i:i+2]]
            i+=2
         else:
            result+=singdoubles[s[i]]
            i+=1
        return result
roman1= Solution()
print(roman1.romanToInt("III"))
