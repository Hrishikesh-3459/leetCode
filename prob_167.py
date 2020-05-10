import copy
def twoSum(numbers,target):
    out = []
    for num in range(len(numbers)):
        diff = target - numbers[num]
        temp_nums = copy.copy(numbers)
        temp_nums.pop(num)
        if (diff in temp_nums):
            out.append(num + 1)
            out.append(temp_nums.index(diff)+2)
            return (out)

print(twoSum([2,7,11,15],9))