class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        res = {}
        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in res and res[diff] != i:
                return [res[diff], i]
            else:
                res[nums[i]] = i