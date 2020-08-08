class Solution:
    def validateStackSequences(self, pushed, popped):
        stack = []
        for i in pushed:
            if i == popped[0]:
                popped.pop(0)
                if stack:
                    while True and stack:
                        if stack[-1] != popped[0]:
                            break
                        stack.pop()
                        popped.pop(0)
            else:
                stack.append(i)
        return len(popped) == 0