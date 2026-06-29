class Solution:
    def reverse(self, nums:list, start:int, end:int):
        while start<end:
            nums[start], nums[end] = nums[end], nums[start]
            start += 1
            end -= 1
    
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        # Reduce k to avoid repetitions
        k %= len(nums)

        # Reverse the array
        self.reverse(nums, 0, len(nums)-1)

        # Reverse the first k elements
        self.reverse(nums, 0, k-1)

        # Reverse the rest of the elements
        self.reverse(nums, k, len(nums)-1)


        