class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        new = []
        for i in range(len(arr)-1):
            val = max(arr[i+1:])
            new.append(val)
        new.append(-1)
        return new
            
