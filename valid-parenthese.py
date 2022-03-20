"""
https://leetcode.com/problems/valid-parentheses/submissions/
"""
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        dis = {")":"(", "}":"{","]":"[" }
        
        for p in s:
            if p in dis.values():
                stack.append(p)
            elif stack and dis[p] == stack[-1]:
                stack.pop()
            else:
                return False
            
        return stack == []
                
        
        