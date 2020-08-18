class Solution:
    def reorderLogFiles(self, logs):
        def custom(log):
            ids, rest = log.split(" ", 1)
            if rest[0].isalpha():
                return (0, rest, ids)
            return (1, )
        return sorted(logs, key = custom)
        
            