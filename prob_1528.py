
def restoreString(s, indices):
    ans = [0] * len(s)
    for i, j in zip(s, indices):
        ans[j] = i
    return ''.join(ans)