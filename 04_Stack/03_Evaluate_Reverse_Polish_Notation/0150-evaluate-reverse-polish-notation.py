"""
Problem: LeetCode 150 - Evaluate Reverse Polish Notation

Key Idea:
To evaluate a given reverse Polish notation expression, we can use a stack data structure. We iterate through the tokens in the expression, and for each token, if it is a number, we push it onto the stack. If it is an operator ('+', '-', '*', '/'), we pop the top two elements from the stack, apply the operator to them, and push the result back onto the stack. At the end, the top element of the stack will be the final result of the expression.

Time Complexity:
The time complexity of this solution is O(n), where n is the number of tokens in the expression. We iterate through the tokens once, and each operation (pushing, popping, and applying operators) takes constant time.

Space Complexity:
The space complexity is O(n), where n is the number of tokens in the expression. In the worst case, the stack could store all tokens from the input expression.
"""


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for c in tokens:
            if c == "+":
                stack.append(stack.pop() + stack.pop())
            elif c == "-":
                a,b = stack.pop(), stack.pop()
                stack.append(b-a)
            elif c == "*":
                stack.append(stack.pop()*stack.pop())
            elif c == "/":
                a,b = stack.pop(), stack.pop()
                stack.append(int(b/a))
            else:
                stack.append(int(c))
        return stack[0]
