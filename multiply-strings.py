class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        string1 = 0
        for i in num1:
            string1 = string1 * 10 + (ord(i) - 48)    
            # ord is used because we want ascii value... and we subtract 48 because 48 is the ascii value of 0 ..... eg - 57-48= 9 string1 = string1 * 10 + (ord(i) - 48)....57 is a ascii value of 9
            
        string2=0
        for i in num2:
            string2 = string2 * 10 + (ord(i) - 48)
            
            
        return str(string1* string2)
            
            
            
        