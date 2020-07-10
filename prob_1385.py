def findTheDistanceValue(arr1, arr2, d):
    di = {}
    for n,i in enumerate(arr1):
        ans = 0
        for j in arr2:
            if (abs(i - j) <= d):
                ans += 1
        di[n] = ans
    x = list(di.values())
    print(x)
    return x.count(0)