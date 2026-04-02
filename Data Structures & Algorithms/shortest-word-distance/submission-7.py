class Solution:
    def shortestDistance(self, wordsDict: List[str], word1: str, word2: str) -> int:
        w1, w2 = -1,-1
        minD = len(wordsDict)

        for i, x in enumerate(wordsDict):
            if x == word1:
                w1 = i
            elif x == word2:
                w2 = i
            if w1 != -1 and w2 != -1:
                minD = min(minD, abs(w2-w1))
        minD = min(minD, abs(w2-w1))
        return minD