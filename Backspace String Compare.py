# Day 9
# Backspace String Compare
# Given two strings S and T, return if they are equal when both are 
# typed into empty text editors. # means a backspace character.
# Input: S = "ab#c", T = "ad#c"
# Output: true
# Explanation: Both S and T become "ac".

# Input: S = "ab##", T = "c#d#"
# Output: true
# Explanation: Both S and T become "".

# Input: S = "a##c", T = "#a#c"
# Output: true
# Explanation: Both S and T become "c".

# Input: S = "a#c", T = "b"
# Output: false
# Explanation: S becomes "c" while T becomes "b".

class Solution(object):
    def backspaceCompare(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: bool
        """
        
        stackS = []
        
        for character in S:
            if character == '#' and len(stackS) != 0:
                stackS.pop()
            elif character != '#':
                stackS.append(character)
        
        stackT = []
        
        for character in T:
            if character == '#' and len(stackT) != 0:
                stackT.pop()
            elif character != '#':
                stackT.append(character)
        
        finalS = "".join(stackS)
        finalT = "".join(stackT)
        
        return stackS == stackT