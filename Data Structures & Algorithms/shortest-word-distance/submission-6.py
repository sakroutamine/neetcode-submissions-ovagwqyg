class Solution:
    def shortestDistance(self, wordsDict: List[str], word1: str, word2: str) -> int:
        iw1, iw2 = -1, -1
        minD = len(wordsDict)
        for i,x in enumerate(wordsDict):
            if x == word1:
                iw1 = i
            elif x == word2:
                iw2 = i
            print(i, x, iw1, iw2)
            if iw1 >=0 and iw2>=0:
                minD = min(abs(iw1-iw2), minD)

        return minD