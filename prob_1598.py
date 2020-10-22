class Solution:
    def minOperations(self, logs) -> int:
        stack = []
        for log in logs:
            if log == "../":
                if stack:
                    stack.pop()
            elif log != "./":
                stack.append(log)
        return len(stack)
