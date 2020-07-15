def queryString(self, S: str, N: int) -> bool:
    for i in range(1, N+1):
        x = "{0:b}".format(i)
        if x not in S:
            return False
    return True