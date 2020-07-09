def numberOfLines(widths, S):
    alpha = {}
    for i in range(26):
        alpha[chr(i + 97)] = widths[i]
    lines = []
    tmp = 0
    for i in S:
        tmp += alpha[i]
        if tmp > 100:
            lines.append(tmp)
            tmp = alpha[i]
    return [len(lines) + 1, tmp]