class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        res = {}
        for i in range(len(nums)):
            if nums[i] in res:
                return True
            res[nums[i]] = i
        return False