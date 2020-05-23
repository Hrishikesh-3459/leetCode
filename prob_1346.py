class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        for i in range(len(arr)):
            x = arr[:i] + arr[i+1:]
            if (arr[i]/2 in x):
                return True
        return False
