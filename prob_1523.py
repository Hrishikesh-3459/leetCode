def countOdds(low, high):
    nums = (high - low + 1)
    if nums & 1 == 0:
        return nums // 2
    if low & 1 == 1 or high & 1 == 1:
        return (nums // 2) + 1
    return nums // 2