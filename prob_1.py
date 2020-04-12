def twoSum(nums, target):
    h = {}
    for i, num in enumerate(nums):
        n = target - num
        if n not in h:
            h[num] = i
        else:
            return [h[n], i]

inp = []
n = int(input("Enter the number of elements in the list: "))
print("Enter the elements")
for i in range(n):
    inp.append(int(input()))
target = int(input("Enter the target: "))
print(twoSum(inp, target))