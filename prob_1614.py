class Solution:
    def maxDepth(self, s: str) -> int:
        stack = []
        ans = 0
        for i in s:
            if i == ')':
                ans = max(ans, len(stack))
                stack.pop()
            elif i == '(':
                stack.append(i)
        return ans
