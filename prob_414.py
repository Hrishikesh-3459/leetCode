<<<<<<< HEAD
def thirdMax(nums):
    # y = list(set(nums)).sort(reverse = True)
    y = sorted(list(set(nums)))
    y = y[::-1]
    print(y)
    if (len(y) < 3):
        return max(y)
    else:
        return y[2]

print(thirdMax([2, 2, 3, 1]))
=======
class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        y = sorted(list(set(nums)))
        y = y[::-1]
        if (len(y) < 3):
            return max(y)
        else:
            return y[2]
        
>>>>>>> c342f33c5f94635b5901867b435c2165820ee334
