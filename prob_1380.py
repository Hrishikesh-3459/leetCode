class Solution:
    def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:
        ans = []
        col_max = []
        
        for i in range(len(matrix[0])):
            x = []
            for j in range(len(matrix)):
                x.append(matrix[j][i])
            col_max.append(max(x))
            
        
        for i in matrix:
            if (min(i) in col_max):
                ans.append(min(i))
                
        return ans
        
            
                
