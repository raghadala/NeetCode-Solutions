"""
Problem: LeetCode 22 - Generate Parentheses

Key Idea:
To generate all valid combinations of parentheses, we can use backtracking. We start with an empty string and two counters, one for the open parentheses and one for the close parentheses. At each step, we have two choices: add an open parenthesis if the count of open parentheses is less than the total number of pairs, or add a close parenthesis if the count of close parentheses is less than the count of open parentheses. We continue this process recursively until we reach the desired length of the string. If the string becomes valid, we add it to the result.

Time Complexity:
The time complexity of this solution is O(4^n / sqrt(n)), where n is the number of pairs of parentheses. This is because each valid combination is a sequence of open and close parentheses of length 2n, and there are 2^(2n) such sequences. However, not all sequences are valid, and the Catalan number (4^n / sqrt(n)) bounds the number of valid combinations.

Space Complexity:
The space complexity is O(4^n / sqrt(n)) * 2n call stack takes 2n open/close paren multiply by combinations
"""


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        stack = [] #hold parentheses
        res = []  #hold list of the output

        def backtrack(openN, closedN):
            if openN == closedN == n:
                res.append("".join(stack)) #joins all the elements in the stack into a single string without any separator between them.
                return

            if openN < n:
                stack.append("(")
                backtrack(openN + 1, closedN) #continue building the sequence
                stack.pop()  #undo the last step to try new combinations
            if closedN < openN:
                stack.append(")")
                backtrack(openN, closedN + 1)
                stack.pop()

        backtrack(0, 0)
        return res
