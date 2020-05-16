def findTheDifference(s, t):
    x =list(t)
    for i in s:
        x.remove(i)

    print(x[0])

findTheDifference('a', 'aa')