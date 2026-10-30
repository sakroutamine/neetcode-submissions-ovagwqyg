class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic = defaultdict(list)
        for i in strs:
            arr = [0]*26

            for j in i:
                arr[ord(j)-ord('a')]+=1
            # print(i)
            dic[str(arr)].append(i)
        # print(dic.values())
        return list(dic.values())