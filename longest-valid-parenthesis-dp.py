"""
this is a question from leetcode 
https://leetcode.com/problems/longest-valid-parentheses/submissions/
"""
class Solution:
    def longestValidParentheses(self, s: str) -> int:
        stack = [-1]
        result = 0
        for i in range(len(s)):
            if (s[i] == "("):
                stack.append(i)
                
            else:
                stack.pop()
                if len(stack)==0:
                    stack.append(i)
                    
                else:
                    result = max(result,(i-stack[-1]))
                    
        return result