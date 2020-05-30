class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        s_stack = []
        t_stack = []
        for i in S:
            if (i != "#"):
                s_stack.append(i)

            elif (i == "#" and len(s_stack) != 0):
                s_stack.pop()



        for j in T:
            if (j != "#"):
                t_stack.append(j)

            elif (j == "#" and len(t_stack) != 0):
                t_stack.pop()

        return s_stack == t_stack
        
