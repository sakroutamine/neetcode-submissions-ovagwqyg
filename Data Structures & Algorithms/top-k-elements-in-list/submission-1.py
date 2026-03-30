class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dic=defaultdict(int)
        arr=[[]for i in range(len(nums)+1)]
        
        for i in nums:
            dic[i] +=1
        print(arr)
        for x,i in dic.items():
            arr[i].append(x)
        res = []

        for i in range(len(arr)-1, 0, -1):
            for n in arr[i]:
                res.append(n)
                if len(res) ==k:
                    return res