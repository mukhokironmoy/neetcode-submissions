class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        # Initilaise left and right sum
        left_sum = 0
        right_sum = sum(nums)

        for i in range(len(nums)):
            # Find the right sum for current index by removing the value from right sum
            right_sum -= nums[i]

            # Check
            if left_sum == right_sum:
                return i

            # Update the left sum
            left_sum += nums[i]

        return -1