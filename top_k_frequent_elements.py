class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        max_freq = len(nums)
        count = Counter(nums)
        buckets = [[] for _ in range(max_freq+1)]

        for num, freq in count.items():
            buckets[freq].append(num)
        
        res = []
        for i in range(max_freq, -1, -1):
            for num in buckets[i]:
                res.append(num)
                if len(res) == k:
                    return res