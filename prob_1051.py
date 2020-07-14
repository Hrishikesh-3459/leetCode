def heightChecker(heights) :
    target = sorted(heights)
    ans = 0
    for i,j in zip(target, heights):
        if i != j:
            ans += 1
    return ans