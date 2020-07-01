class Solution:
    def numSmallerByFrequency(self, queries: List[str], words: List[str]) -> List[int]:
        ans = []
        for q in queries:
            q_count = q.count(min(q))
            tmp = 0
            for w in words:
                w_count = w.count(min(w))
                if q_count < w_count:
                    tmp += 1
            ans.append(tmp)
        return ans
