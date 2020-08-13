class Solution:
    def areSentencesSimilar(self, words1, words2, pairs):
        if len(words1) != len(words2):
            return False
        for i, j in zip(words1, words2):
            if i != j:
                if [i,j] not in pairs and [j,i] not in pairs:
                    return False
        return True