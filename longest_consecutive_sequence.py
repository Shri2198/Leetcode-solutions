class Solution:
    def longestConsecutive(self, nums: List[int]) -> bool:
        if not nums:
            return 0
            
        num_set = set(nums)  
        res = 0
        
        for i in num_set:  
            if i - 1 not in num_set:  
                cur_len = 1
                cur_num = i
                while cur_num + 1 in num_set:  
                    cur_len += 1
                    cur_num += 1
                res = max(res, cur_len)
        return res