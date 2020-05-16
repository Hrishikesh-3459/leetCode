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