class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        opts = defaultdict(list)
        for i in strs:
            dic = [0]*26
            for j in i:
                dic[ord(j)-ord('a')] +=1
            opts[tuple(dic)].append(i)
        return list(opts.values())