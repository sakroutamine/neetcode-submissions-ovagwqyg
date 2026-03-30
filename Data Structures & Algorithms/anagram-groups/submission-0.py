class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic=defaultdict(list)
        for i in strs:
            arr = [0]*26
            for j in i:
                arr[ord(j)-ord('a')] += 1
            dic[tuple(arr)].append(i)
        return list(dic.values())
