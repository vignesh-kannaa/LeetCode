"""Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

 

Example 1:

Input: n = 3
Output: ["((()))","(()())","(())()","()(())","()()()"]
Example 2:

Input: n = 1
Output: ["()"]"""


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        stack = []
        res = []

        def backtrack(openCount, closeCount):
            if openCount == closeCount == n:
                res.append("".join(stack))
                return
            if openCount < n:
                stack.append('(')
                backtrack(openCount+1, closeCount)
                stack.pop()  # pop since to use previous in different tree branch
            if closeCount < openCount:
                stack.append(')')
                backtrack(openCount, closeCount+1)
                stack.pop()  # pop since to use previous in different tree branch
        backtrack(0, 0)
        return res


"""1)add open ( when opencount is < n
   2)add close ) when closecount is < opencount
   3)base case: both are equal to n"""
