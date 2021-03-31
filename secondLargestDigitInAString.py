class Solution:
    def secondHighest(self, s: str) -> int:
        numbers = []
        for i in s:
            if i.isdigit():
                numbers.append(int(i))
        if len(list(set(numbers))) <= 1:
            return -1
        return sorted(list(set(numbers)), reverse = True)[1]
