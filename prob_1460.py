class Solution:
    def canBeEqual(self, target: List[int], arr: List[int]) -> bool:
        if (set(target) != set(arr)):
            return False
        return True
        
