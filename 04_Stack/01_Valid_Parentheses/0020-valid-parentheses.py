"""
Problem: LeetCode 20 - Valid Parentheses

Key Idea:
To determine if a given string of parentheses 's' is valid, we can use a stack data structure. We iterate through each character in 's', and if the character is an opening parenthesis ('(', '{', '['), we push it onto the stack. If the character is a closing parenthesis (')', '}', ']'), we check if the stack is empty or if the top element of the stack does not match the current closing parenthesis. If either of these conditions is met, we know the string is not valid. Otherwise, we pop the top element from the stack. At the end, if the stack is empty, the string is valid.

Time Complexity:
The time complexity of this solution is O(n), where n is the length of the input string 's'. We iterate through the string once, and each operation (pushing or popping from the stack) takes constant time.

Space Complexity:
The space complexity is O(n), where n is the length of the input string 's'. In the worst case, the stack could store all characters of the input string.
"""

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        Map = {")": "(", "]": "[", "}": "{"}

        for c in s:
            if c in Map:
                if stack and stack[-1] == Map[c]:
                    stack.pop()
                else:
                    return False
            
            else:
                stack.append()
        
        return True if not stack else False

class Solution:
    def isValid(self, s: str) -> bool:
        Map = {")": "(", "]": "[", "}": "{"}
        stack = []

        for c in s:
            if c not in Map: # c is an opening bracket
                stack.append(c)
                continue  #move to next character
            if not stack or stack[-1] != Map[c]:  #if empty or top of stack doesnt match opening bracket
                return False
            stack.pop()  #pop top element as it matches closing paren

        return not stack   # if stack is empty return true otherwise false
    
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        paren = {")":"(", "]":"[","}":"{"}

        for p in s:
            if p in paren.values():
                stack.append(p)
            elif p in paren:
                if not stack or stack[-1] != paren[p]: #the most recent opening bracket does not match this closing bracket.
                    return False
                stack.pop()
        return not stack

