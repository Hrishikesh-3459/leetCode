class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        ans = []
        for i in arr2:
            while(arr1.count(i)):
                ans.append(i)
                arr1.remove(i)
                
                
        
        ans.extend(sorted(arr1))
        return ans
        
