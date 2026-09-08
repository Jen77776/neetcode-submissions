class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #count appear times using hashmap index-number value-times
        # 1:1 2:2 3:3
        # create bucket index-appear times value-number array
        #[[],[1],[2],[3]]
        count={}
        for num in nums:
            count[num]=count.get(num,0)+1
        buckets=[[]for _ in range(len(nums)+1)]
        for num, freq in count.items():
            buckets[freq].append(num)
        res=[]
        for i in range(len(nums),0,-1):
            for num in buckets[i]:
                res.append(num)
                if len(res)==k:
                    return res
        return res
