class Solution:
    def threeSum(self, nums):
        nums.sort()
        seen = set()
        ans = []
        for n,i in enumerate(nums):
            if i > 0:
                return ans
            elif i in seen:
                continue
            else:
                ret = self.twoSum(nums, n)
                if ret:
                    ans.extend(ret)
                seen.add(i)
        return ans
                
            
    def twoSum(self, arr, n):
        low = n + 1
        high = len(arr) - 1
        tmp = []
        while low < high:
            cur = arr[n] + arr[low] + arr[high]
            if cur < 0:
                low += 1
            elif cur > 0:
                high -= 1
            else:
                tmp.append([arr[n], arr[low], arr[high]])
                high -= 1
                low += 1
                while low < high and arr[low] == arr[low - 1]:
                    low += 1
        return tmp