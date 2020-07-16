def isAlienSorted(words, order):
    big = len(sorted(words, key = len)[-1])
    for i in range(len(words)):
        if len(words[i]) == big:
            continue
        dif = big - len(words[i])
        spaces = "0" * dif
        words[i] += spaces
    order = "0" + order
    i = 0
    j = 1
    k = 0
    while True:
        if order.index(words[i][k]) > order.index(words[j][k]):
            return False
        if order.index(words[i][k]) < order.index(words[j][k]):
            if j + 1 == len(words):
                return True
            i += 1
            j += 1
            k = 0
        if words[i][k] == words[j][k]:
            k += 1