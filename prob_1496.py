import copy
class Solution:
    def isPathCrossing(self, path: str) -> bool:
        pos = [0, 0]
        visited = [[0, 0]]
        for i in path:
            print(visited)
            if i == 'N':
                pos[1] += 1
                if pos in visited:
                    return True
                val = copy.copy(pos)
                visited.append(val)
            elif i == 'S':
                pos[1] -= 1
                if pos in visited:
                    return True
                val = copy.copy(pos)
                visited.append(val)
            elif i == 'E':
                pos[0] += 1
                if pos in visited:
                    return True
                val = copy.copy(pos)
                visited.append(val)
            elif i == 'W':
                pos[0] -= 1
                if pos in visited:
                    return True
                val = copy.copy(pos)
                visited.append(val)
        print(visited)
        return False
