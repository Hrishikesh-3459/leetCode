class Solution:
    def sortedSquares(self, A: List[int]) -> List[int]:
        x = list(map(lambda x: x ** 2, A))
        return sorted(x)
        
