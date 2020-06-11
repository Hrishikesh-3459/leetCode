class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        if not nums:
            return 
        x = nums[:n]
        y = nums[n:]
        ans = []
        for i,r in zip(x, y):
            ans.append(i)
            ans.append(r)
        return ans
