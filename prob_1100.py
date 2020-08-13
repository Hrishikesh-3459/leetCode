class Solution:
    def numKLenSubstrNoRepeats(self, S, K):
        if K > len(S):
            return 0
        ans = 0
        start = 0
        stop = start + K
        q = list(S[start:stop])
        if len(q) == len(set(q)):
            ans += 1
        while stop < len(S):
            q.pop(0)
            q.append(S[stop])
            stop += 1
            if len(q) == len(set(q)):
                ans += 1
        return ans