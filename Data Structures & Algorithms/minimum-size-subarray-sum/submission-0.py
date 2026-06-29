class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        min_len = float('inf')

        left = 0
        right = 0
        current_sum = 0

        while right < len(nums):
            current_sum += nums[right]

            while current_sum >= target:
                min_len = min(min_len, right-left+1)
                current_sum -= nums[left]
                left += 1

            right += 1

        return 0 if min_len == float('inf') else min_len