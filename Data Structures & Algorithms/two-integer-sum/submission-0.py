class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        sums = dict({})

        for i in range(len(nums)):
            if target - nums[i] in sums:
                return [sums[target - nums[i]], i]
            sums[nums[i]] = i      