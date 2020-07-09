def canVisitAllRooms(rooms, keys):
    entered = set()
    entered.add(0)
    keys = []
    keys.extend(rooms[0])
    i = 0
    while keys:
        r = keys.pop(0)
        entered.add(r)
        keys.extend(rooms[r])
        if len(entered) == len(rooms):
            return True
        i += 1
        if i == 10000:
            return False
    if len(entered) == len(rooms):
        return True
    return False