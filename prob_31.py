class Solution:
    def nextPermutation(self, nums):
        """
        Do not return anything, modify nums in-place instead.
        """
        flag = True
        for i in range(1, len(nums)):
            if nums[i - 1] < nums[i]:
                flag = False
                break
        if flag == True:
            nums.sort()
            return
        for i in range(len(nums) - 1, 0, -1):
            if nums[i] > nums[i - 1]:
                ind1 = i - 1
                break
        num = nums[ind1]
        # print(ind1, num)
        tmp = num + 1
        while True:
            flag = True
            for i in range(len(nums) - 1, ind1, -1):
                if nums[i] == tmp:
                    flag = False
                    ind2 = i
                    # print(ind2, )
                    break
            if flag == False:
                break
            tmp += 1
        nums[ind1], nums[ind2] = nums[ind2], nums[ind1]
        temp = []
        for i in range(ind1 + 1, len(nums)):
            temp.append(nums.pop())
        nums = nums.extend(temp)