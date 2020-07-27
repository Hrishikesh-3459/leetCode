def canMakeArithmeticProgression(arr):
    arr.sort()
    val = abs(arr[1] - arr[0])
    for i in range(2, len(arr)):
        cur = abs(arr[i] - arr[i-1])
        if cur != val:
            return False
    return True