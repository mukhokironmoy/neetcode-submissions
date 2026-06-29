class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # Track the index where non zero elements need to be inserted
        non_zero_index = 0

        # Move non zero nums to the current non zero index for each iteration
        for num in nums:
            if num != 0:
                nums[non_zero_index] = num
                non_zero_index += 1

        # Make the rest of the indices zero
        while non_zero_index < len(nums):
            nums[non_zero_index] = 0
            non_zero_index += 1
         