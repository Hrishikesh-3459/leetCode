class Solution:
    def removeDuplicates(self, S: str) -> str:
        stack = []
    

        for i in S:
            if (len(stack) != 0):
                val = stack.pop()
                if (i == val):
                    pass
                if (i != val):
                    stack.append(val)
                    stack.append(i)
            else:
                stack.append(i)

        ans = ""
        for i in stack:
            ans += i

        return ans

