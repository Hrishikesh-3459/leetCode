class Solution:
    def countBalls(self, lowLimit: int, highLimit: int) -> int:
        boxes = {}
        for i in range(lowLimit, highLimit + 1):
            suma = 0
            for j in str(i):
                suma += int(j)
            if suma in boxes:
                boxes[suma] += 1
            else:
                boxes[suma] = 1
        return max(list(boxes.values()))
