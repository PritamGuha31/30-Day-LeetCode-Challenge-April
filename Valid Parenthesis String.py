# Day 16
# Valid Parenthesis String
# Given a string containing only three types of characters: '(', ')' and '*', 
# write a function to check whether this string is valid. We define the validity of a string by these rules:

# Any left parenthesis '(' must have a corresponding right parenthesis ')'.
# Any right parenthesis ')' must have a corresponding left parenthesis '('.
# Left parenthesis '(' must go before the corresponding right parenthesis ')'.
# '*' could be treated as a single right parenthesis ')' or a single left parenthesis '(' or an empty string.
# An empty string is also valid.

# Input: "()"
# Output: True

# Input: "(*)"
# Output: True

# Input: "(*))"
# Output: True

class Solution(object):
    def checkValidString(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        starStack = []
        
        for index, char in enumerate(s):
            if char == '(':
                stack.append(index)
            elif char == '*':
                starStack.append(index)
            elif char == ')':
                if len(stack) > 0:
                    stack.pop()
                elif len(starStack) > 0:
                    starStack.pop()
                else :
                    return False
        
        while stack and starStack :
            if stack[-1] < starStack[-1] :
                stack.pop()
                starStack.pop()
            else :
                break
        return len(stack) == 0