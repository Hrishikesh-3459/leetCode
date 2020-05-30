class Solution:
    def calPoints(self, ops: List[str]) -> int:
        stack = []
        i = 0

        while True:
            if(i == len(ops)):
                break

            if(ops[i] == '+'):
                val_1 = stack.pop()
                val_2 = stack.pop()
                stack.append(int(val_2))
                stack.append(int(val_1))
                stack.append(int(val_1) + int(val_2))

            elif(ops[i] == 'D'):
                val = stack.pop()
                stack.append(int(val))
                stack.append(2 * int(val))

            elif(ops[i] == 'C' and stack):
                stack.pop()

            else:
                stack.append(int(ops[i]))
            i += 1

        return sum(stack)
