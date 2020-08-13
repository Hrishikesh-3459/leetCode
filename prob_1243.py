class Solution:
    def transformArray(self, arr):
        while True:
            inc = []
            dec = []
            flag = True
            for i in range(1, len(arr) - 1):
                if arr[i - 1] > arr[i] < arr[i + 1]:
                    inc.append(i)
                    flag = False
                elif arr[i - 1] < arr[i] > arr[i + 1]:
                    dec.append(i)
                    flag = False
            if flag == True:
                return arr
            for i in inc:
                arr[i] += 1
            for j in dec:
                arr[j] -= 1